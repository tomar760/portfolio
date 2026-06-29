(function(){
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const finePointer = window.matchMedia('(pointer: fine)').matches;

  /* ===== THEME (dark default, light toggle) ===== */
  const root = document.documentElement;
  let stored = null;
  try { stored = localStorage.getItem('theme'); } catch(e){}
  if (stored === 'light') root.classList.add('light');
  const themeBtn = document.getElementById('themeToggle');
  if (themeBtn){
    themeBtn.addEventListener('click', () => {
      root.classList.toggle('light');
      try { localStorage.setItem('theme', root.classList.contains('light') ? 'light' : 'dark'); } catch(e){}
    });
  }

  /* ===== MOBILE NAV ===== */
  const burger = document.getElementById('burger');
  const navLinks = document.getElementById('navLinks');
  if (burger && navLinks){
    burger.addEventListener('click', () => { burger.classList.toggle('open'); navLinks.classList.toggle('open'); });
    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => { burger.classList.remove('open'); navLinks.classList.remove('open'); });
    });
  }

  /* ===== SCROLL REVEAL ===== */
  const revealEls = document.querySelectorAll('.reveal');
  if (revealEls.length){
    const ro = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting){ e.target.classList.add('in'); ro.unobserve(e.target); } });
    }, { threshold: 0.12 });
    revealEls.forEach(el => ro.observe(el));
  }

  /* ===== SKILL BARS ===== */
  const skillFills = document.querySelectorAll('.skill-fill');
  if (skillFills.length){
    const so = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting){ e.target.style.width = e.target.dataset.level + '%'; so.unobserve(e.target); } });
    }, { threshold: 0.3 });
    skillFills.forEach(el => so.observe(el));
  }

  /* ===== ACTIVE NAV (in-page sections) ===== */
  const sections = document.querySelectorAll('main section[id]');
  const navAnchors = document.querySelectorAll('.nav-links a[data-sec]');
  if (sections.length && navAnchors.length){
    const no = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting){
          const id = e.target.getAttribute('id');
          navAnchors.forEach(a => a.classList.toggle('active', a.getAttribute('data-sec') === id));
        }
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    sections.forEach(s => no.observe(s));
  }

  /* ===== HERO MOUSE GLOW ===== */
  const heroSection = document.getElementById('heroSection');
  if (heroSection){
    heroSection.addEventListener('mousemove', (e) => {
      const r = heroSection.getBoundingClientRect();
      heroSection.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      heroSection.style.setProperty('--my', (e.clientY - r.top) + 'px');
    });
  }

  /* ===== STAT COUNT-UP ===== */
  const heroStats = document.querySelector('.hero-stats');
  if (heroStats){
    const sto = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting){
          entry.target.querySelectorAll('.stat-number').forEach(el => {
            const target = parseInt(el.dataset.count, 10);
            const suffix = el.dataset.suffix || '';
            if (reduceMotion){ el.textContent = target + suffix; return; }
            let cur = 0; const step = Math.max(target / 40, 0.5);
            const t = setInterval(() => {
              cur += step;
              if (cur >= target){ el.textContent = target + suffix; clearInterval(t); }
              else el.textContent = Math.floor(cur) + suffix;
            }, 30);
          });
          sto.unobserve(entry.target);
        }
      });
    }, { threshold: 0.4 });
    sto.observe(heroStats);
  }

  /* ===== TYPING EFFECT ===== */
  const typedEl = document.getElementById('typedText');
  if (typedEl){
    const words = ['Payroll & Compliance', 'Responsive Web Design', 'AI-Assisted Workflows', 'People Operations', 'Clean, Modern UI'];
    if (reduceMotion){ typedEl.textContent = ' ' + words[0]; }
    else {
      let wi = 0, ci = 0, del = false;
      (function loop(){
        const w = words[wi];
        ci += del ? -1 : 1;
        typedEl.textContent = ' ' + w.substring(0, ci);
        let speed = del ? 35 : 75;
        if (!del && ci === w.length){ speed = 1700; del = true; }
        else if (del && ci === 0){ del = false; wi = (wi + 1) % words.length; speed = 400; }
        setTimeout(loop, speed);
      })();
    }
  }

  /* ===== BACK TO TOP ===== */
  const btt = document.getElementById('backToTop');
  if (btt){
    window.addEventListener('scroll', () => btt.classList.toggle('visible', window.scrollY > 500));
    btt.addEventListener('click', () => window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' }));
  }

  /* ===== CUSTOM CURSOR ===== */
  const dot = document.getElementById('cursorDot');
  const ring = document.getElementById('cursorRing');
  const glow = document.getElementById('cursorGlow');
  if (dot && ring && glow){
    if (finePointer && !reduceMotion){
      root.classList.add('custom-cursor-active');
      let mx = innerWidth/2, my = innerHeight/2, rx = mx, ry = my;
      document.addEventListener('mousemove', (e) => {
        mx = e.clientX; my = e.clientY;
        dot.style.left = mx+'px'; dot.style.top = my+'px';
        glow.style.left = mx+'px'; glow.style.top = my+'px';
      });
      (function animate(){ rx += (mx-rx)*0.16; ry += (my-ry)*0.16; ring.style.left = rx+'px'; ring.style.top = ry+'px'; requestAnimationFrame(animate); })();
      const bind = () => document.querySelectorAll('a, button, .work-card, .skill-panel, .edu-card, .stat-card, .proj-card, .filter-btn').forEach(el => {
        el.addEventListener('mouseenter', () => ring.classList.add('hover'));
        el.addEventListener('mouseleave', () => ring.classList.remove('hover'));
      });
      bind();
      window.__bindCursor = bind;
    } else { dot.style.display='none'; ring.style.display='none'; glow.style.display='none'; }
  }

  /* ===== TILT ON CARDS ===== */
  if (innerWidth > 768 && !reduceMotion){
    const bindTilt = () => document.querySelectorAll('.work-card, .skill-panel, .edu-card, .stat-card, .proj-card').forEach(card => {
      if (card.__tilt) return; card.__tilt = true;
      card.addEventListener('mousemove', (e) => {
        const r = card.getBoundingClientRect();
        const x = e.clientX - r.left, y = e.clientY - r.top;
        const rX = (y - r.height/2)/26, rY = (r.width/2 - x)/26;
        card.style.transform = `perspective(900px) rotateX(${rX}deg) rotateY(${rY}deg) translateY(-4px)`;
      });
      card.addEventListener('mouseleave', () => { card.style.transform = ''; });
    });
    bindTilt();
    window.__bindTilt = bindTilt;
  }

  /* ===== PARTICLE NETWORK ===== */
  const canvas = document.getElementById('particles-canvas');
  if (canvas){
    const ctx = canvas.getContext('2d');
    let particles = [];
    const palette = ['91,140,255','164,99,247','255,111,213'];
    function resize(){ canvas.width = innerWidth; canvas.height = innerHeight; }
    resize();
    class P{ constructor(){ this.reset(); }
      reset(){ this.x=Math.random()*canvas.width; this.y=Math.random()*canvas.height; this.size=Math.random()*1.8+0.6; this.sx=(Math.random()-0.5)*0.4; this.sy=(Math.random()-0.5)*0.4; this.op=Math.random()*0.4+0.15; this.c=palette[Math.floor(Math.random()*palette.length)]; }
      update(){ this.x+=this.sx; this.y+=this.sy; if(this.x<0||this.x>canvas.width)this.sx*=-1; if(this.y<0||this.y>canvas.height)this.sy*=-1; }
      draw(){ ctx.beginPath(); ctx.arc(this.x,this.y,this.size,0,Math.PI*2); ctx.fillStyle=`rgba(${this.c},${this.op})`; ctx.fill(); }
    }
    function init(){ const n=Math.min(60,Math.floor((canvas.width*canvas.height)/19000)); particles=[]; for(let i=0;i<n;i++)particles.push(new P()); }
    init();
    function conn(){ for(let i=0;i<particles.length;i++)for(let j=i+1;j<particles.length;j++){ const dx=particles[i].x-particles[j].x, dy=particles[i].y-particles[j].y, d=Math.sqrt(dx*dx+dy*dy); if(d<110){ ctx.beginPath(); ctx.moveTo(particles[i].x,particles[i].y); ctx.lineTo(particles[j].x,particles[j].y); ctx.strokeStyle=`rgba(${particles[i].c},${0.07*(1-d/110)})`; ctx.lineWidth=0.6; ctx.stroke(); } } }
    function loop(){ ctx.clearRect(0,0,canvas.width,canvas.height); particles.forEach(p=>{p.update();p.draw();}); conn(); requestAnimationFrame(loop); }
    if (reduceMotion){ particles.forEach(p=>p.draw()); } else { loop(); }
    window.addEventListener('resize', () => { resize(); init(); if(reduceMotion){ ctx.clearRect(0,0,canvas.width,canvas.height); particles.forEach(p=>p.draw()); } });
  }

  /* ===== PROJECTS FILTER ===== */
  const filterBar = document.getElementById('filterBar');
  if (filterBar){
    const cards = Array.from(document.querySelectorAll('.proj-card'));
    const countEl = document.getElementById('projCount');
    const noRes = document.getElementById('noResults');
    const searchInput = document.getElementById('projSearch');
    let activeCat = 'All';
    function apply(){
      const q = (searchInput ? searchInput.value : '').trim().toLowerCase();
      let shown = 0;
      cards.forEach(c => {
        const cat = c.dataset.cat;
        const txt = (c.dataset.search || '').toLowerCase();
        const matchCat = activeCat === 'All' || cat === activeCat;
        const matchQ = !q || txt.includes(q);
        const vis = matchCat && matchQ;
        c.style.display = vis ? '' : 'none';
        if (vis) shown++;
      });
      if (countEl) countEl.textContent = shown + (shown === 1 ? ' project' : ' projects') + (activeCat !== 'All' ? ' in ' + activeCat : '');
      if (noRes) noRes.style.display = shown === 0 ? 'block' : 'none';
    }
    filterBar.querySelectorAll('.filter-btn').forEach(b => {
      b.addEventListener('click', () => {
        filterBar.querySelectorAll('.filter-btn').forEach(x => x.classList.remove('active'));
        b.classList.add('active');
        activeCat = b.dataset.filter;
        apply();
      });
    });
    if (searchInput) searchInput.addEventListener('input', apply);
    apply();
  }

  /* ===== CONTACT FORM (mailto) ===== */
  const form = document.getElementById('contactForm');
  if (form){
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = encodeURIComponent(form.name.value || '');
      const email = encodeURIComponent(form.email.value || '');
      const msg = encodeURIComponent(form.message.value || '');
      const body = `Name: ${decodeURIComponent(name)}%0D%0AEmail: ${decodeURIComponent(email)}%0D%0A%0D%0A${decodeURIComponent(msg)}`;
      window.location.href = `mailto:tomaraditya760@gmail.com?subject=Portfolio enquiry from ${decodeURIComponent(name)}&body=${body}`;
      const status = document.getElementById('formStatus');
      if (status) status.textContent = 'Opening your email app…';
    });
  }
})();
