#!/usr/bin/env python3
import os, html

HERE = os.path.dirname(os.path.abspath(__file__))
CSS = open(os.path.join(HERE, "assets", "theme.css")).read()
JS = open(os.path.join(HERE, "assets", "app.js")).read()

EMAIL = "tomaraditya760@gmail.com"
GITHUB = "https://github.com/tomar760"  # GitHub profile

FONT = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700'
        '&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">')

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("services.html", "Services"),
    ("projects.html", "GitHub"),
    ("contact.html", "Contact"),
]

def nav(active):
    links = ""
    for href, label in NAV_ITEMS:
        cls = ' class="active"' if href == active else ''
        links += f'<li><a href="{href}"{cls}>{label}</a></li>'
    return f'''<header>
  <nav>
    <a href="index.html" class="logo"><span class="mark"></span>Aditya Tomar</a>
    <div class="nav-right">
      <ul class="nav-links" id="navLinks">
        {links}
        <li><a href="contact.html" class="nav-cta">Hire Me</a></li>
      </ul>
      <button class="theme-toggle" id="themeToggle" aria-label="Toggle light / dark mode" title="Toggle theme">
        <svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
        <svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4.5"/><path d="M12 1.5v2M12 20.5v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M1.5 12h2M20.5 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"/></svg>
      </button>
      <button class="burger" id="burger" aria-label="Toggle menu"><span></span><span></span><span></span></button>
    </div>
  </nav>
</header>'''

def footer():
    fl = ""
    for href, label in NAV_ITEMS:
        fl += f'<a href="{href}">{label}</a>'
    fl += '<a href="terms.html">Terms</a><a href="privacy.html">Privacy</a>'
    return f'''<footer>
  <div class="divider" style="margin-bottom:18px;"><span></span><span></span><span></span></div>
  <nav class="footer-nav">{fl}</nav>
  &copy; 2026 Aditya Tomar · Surat, Gujarat, India · <a href="mailto:{EMAIL}">{EMAIL}</a>
</footer>'''

def page(filename, title, desc, body, active, has_hero=False):
    main_id = ' id="top"'
    html_doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
{FONT}
<style>
{CSS}
</style>
</head>
<body>

<canvas id="particles-canvas" aria-hidden="true"></canvas>
<div class="bg-blobs" aria-hidden="true">
  <div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div>
</div>
<div class="cursor-glow" id="cursorGlow" aria-hidden="true"></div>
<div class="cursor-ring" id="cursorRing" aria-hidden="true"></div>
<div class="cursor-dot" id="cursorDot" aria-hidden="true"></div>

{nav(active)}

<main{main_id}>
{body}
</main>

{footer()}

<button class="back-to-top" id="backToTop" aria-label="Back to top">
  <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
</button>

<script>
{JS}
</script>
</body>
</html>'''
    with open(os.path.join(HERE, filename), "w") as f:
        f.write(html_doc)
    print("wrote", filename)


# ============ HOME ============
home_body = '''  <section class="hero" id="heroSection">
    <div class="hero-grid" aria-hidden="true"></div>
    <div class="wrap">
      <div class="hero-copy">
        <div class="eyebrow">Surat, Gujarat · Open to opportunities</div>
        <h1>Aditya<br>Tomar</h1>
        <div class="role-line">HR Executive <span class="x">×</span> Freelance Web Developer</div>
        <div class="type-line">Currently into:<span id="typedText"></span><span class="type-cursor">|</span></div>
        <p class="tagline">I keep people operations running smoothly by day — payroll, compliance, recruitment — and build clean, modern, fully responsive websites on the side, often leaning on AI tools to move faster without cutting corners. Two different crafts, the same habit of getting the details right.</p>
        <div class="btn-row">
          <a href="contact.html" class="btn btn-primary">Let's talk →</a>
          <a href="projects.html" class="btn btn-ghost">Browse GitHub projects</a>
        </div>
        <div class="meta-row">
          <span><span class="dot"></span>Surat, Gujarat, India</span>
          <span><span class="dot"></span>''' + EMAIL + '''</span>
        </div>
        <div class="hero-stats">
          <div class="stat-block"><span class="stat-number" data-count="3" data-suffix="+">0</span><div class="stat-label">Years in HR</div></div>
          <div class="stat-block"><span class="stat-number" data-count="2" data-suffix="">0</span><div class="stat-label">Crafts Mastered</div></div>
          <div class="stat-block"><span class="stat-number" data-count="100" data-suffix="%">0</span><div class="stat-label">Responsive Builds</div></div>
        </div>
      </div>
      <div class="orb-stage" aria-hidden="true">
        <div class="orb-cluster">
          <div class="orbit-ring-2"></div>
          <div class="orb-ring"></div>
          <div class="orb o1"></div>
          <div class="orb o2"></div>
          <div class="orb o3"></div>
          <div class="orb-core"></div>
        </div>
      </div>
    </div>
    <a href="#snapshot" class="scroll-indicator" aria-label="Scroll down">
      <span class="mouse"></span>
      <span>Scroll</span>
    </a>
  </section>

  <section id="snapshot">
    <div class="wrap">
      <div class="section-head reveal">
        <div class="eyebrow">Snapshot</div>
        <h2>Two disciplines, one mindset.</h2>
        <p>Structured on one side, creative on the other — both run on the same attention to detail.</p>
      </div>
      <div class="about-grid">
        <div class="about-text reveal">
          <p>Since <strong>June 2023</strong>, I've worked as an <strong>HR Executive</strong>, managing the full employee lifecycle — attendance, payroll, statutory compliance, recruitment coordination, and grievance handling — on Siebel HR software. It's a role built on accuracy.</p>
          <p>Outside HR hours, I build fully responsive websites with HTML, CSS and JavaScript, and make good use of <strong>AI tools</strong> to ship polished layouts faster without compromising on quality.</p>
          <div class="btn-row" style="margin-bottom:0;">
            <a href="about.html" class="btn btn-ghost">More about me →</a>
            <a href="services.html" class="btn btn-ghost">What I offer →</a>
          </div>
        </div>
        <div class="stat-card reveal">
          <div class="row"><span class="label">LOCATION</span><span class="value">Surat, Gujarat, India</span></div>
          <div class="row"><span class="label">CURRENT ROLE</span><span class="value">HR Executive</span></div>
          <div class="row"><span class="label">HR SOFTWARE</span><span class="value">Siebel HR</span></div>
          <div class="row"><span class="label">LANGUAGES</span><span class="value">Hindi, English</span></div>
          <div class="row"><span class="label">PASSPORT</span><span class="value">Valid</span></div>
          <div class="badges">
            <span class="badge"><span class="dot"></span>Open to relocation</span>
            <span class="badge"><span class="dot"></span>Builds with AI tools</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section id="skills">
    <div class="wrap">
      <div class="section-head reveal">
        <div class="eyebrow">Skills</div>
        <h2>What I bring to the table.</h2>
        <p>A blend of operational HR expertise and hands-on front-end development.</p>
      </div>
      <div class="skills-grid">
        <div class="skill-panel hr reveal">
          <h3><span class="tag"></span>HR Operations</h3>
          ''' + ''.join([f'<div class="skill-item"><div class="top"><span>{n}</span><span>{l}%</span></div><div class="skill-bar"><div class="skill-fill" data-level="{l}"></div></div></div>' for n,l in [("Payroll & Attendance Management",92),("HR MIS & Advanced Excel",90),("Statutory Compliance (PF & ESIC)",88),("Recruitment & Onboarding",85),("Employee Relations",85),("Siebel HR Software",80)]]) + '''
        </div>
        <div class="skill-panel dev reveal">
          <h3><span class="tag"></span>Web Development</h3>
          ''' + ''.join([f'<div class="skill-item"><div class="top"><span>{n}</span><span>{l}%</span></div><div class="skill-bar"><div class="skill-fill" data-level="{l}"></div></div></div>' for n,l in [("HTML5 & CSS3",85),("AI-Assisted Web Development",88),("Responsive Web Design",85),("JavaScript (ES6+)",75),("UI/UX Fundamentals",75),("Git & Version Control",70),("Performance & SEO Basics",68)]]) + '''
        </div>
      </div>
    </div>
  </section>

  <section id="home-cta">
    <div class="wrap">
      <div class="cta-strip reveal">
        <div class="eyebrow" style="justify-content:center;">Let's connect</div>
        <h2>Have a project or a role in mind?</h2>
        <p>Open to HR roles in India and abroad, freelance web builds, or just a good conversation.</p>
        <div class="contact-actions" style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;">
          <a href="contact.html" class="btn btn-primary">Get in touch →</a>
          <a href="projects.html" class="btn btn-ghost">See the code library</a>
        </div>
      </div>
    </div>
  </section>'''
page("index.html", "Aditya Tomar — HR Executive & Freelance Web Developer",
     "Portfolio of Aditya Tomar — HR Executive at Tata Motors, Surat, and freelance web developer.",
     home_body, "index.html", has_hero=True)


# ============ ABOUT ============
about_body = '''  <section class="page-pad" id="about">
    <div class="wrap">
      <div class="section-head reveal">
        <div class="eyebrow">About</div>
        <h2>Two disciplines, one mindset.</h2>
        <p>Structured on one side, creative on the other — both run on the same attention to detail.</p>
      </div>
      <div class="about-grid">
        <div class="about-text reveal">
          <p>Since <strong>June 2023</strong>, I've worked as an <strong>HR Executive</strong>, managing the full employee lifecycle — attendance, payroll, statutory compliance, recruitment coordination, and grievance handling — on Siebel HR software. It's a role built on accuracy: salary sheets that balance, records that hold up to audits, and people who feel heard.</p>
          <p>Outside of HR hours, I work as a <strong>freelance web developer</strong>, designing and building fully responsive websites with HTML, CSS and JavaScript — and I make good use of <strong>AI tools</strong> to move faster, write cleaner code, and ship polished layouts without compromising on quality. It scratches a different itch — turning a blank page into something clean and functional — but it draws on the same instinct I use in HR: organize first, then execute precisely.</p>
          <p>I'm currently looking to grow further in HR — in India and ideally abroad across the <strong>Gulf and Europe</strong> — while continuing to take on freelance development projects on the side.</p>
        </div>
        <div class="stat-card reveal">
          <div class="row"><span class="label">LOCATION</span><span class="value">Surat, Gujarat, India</span></div>
          <div class="row"><span class="label">CURRENT ROLE</span><span class="value">HR Executive</span></div>
          <div class="row"><span class="label">HR SOFTWARE</span><span class="value">Siebel HR</span></div>
          <div class="row"><span class="label">LANGUAGES</span><span class="value">Hindi, English</span></div>
          <div class="row"><span class="label">PASSPORT</span><span class="value">Valid</span></div>
          <div class="badges">
            <span class="badge"><span class="dot"></span>Open to relocation</span>
            <span class="badge"><span class="dot"></span>Builds with AI tools</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section id="experience">
    <div class="wrap">
      <div class="section-head reveal">
        <div class="eyebrow">Experience</div>
        <h2>Where I've put it to work.</h2>
      </div>
      <div class="timeline reveal">
        <div class="tl-item">
          <div class="when">June 2023 — Present</div>
          <h3>HR Executive</h3>
          <div class="org">Tata Motors, Surat</div>
          <ul>
            <li>Manage daily attendance, leave records and workforce data</li>
            <li>Prepare and maintain accurate monthly salary sheets</li>
            <li>Coordinate recruitment activities, interview scheduling and onboarding</li>
            <li>Ensure ongoing compliance with PF & ESIC regulations</li>
            <li>Handle employee queries, grievances and HR documentation</li>
            <li>Generate HR reports and MIS for senior management on Siebel HR software</li>
          </ul>
        </div>
        <div class="tl-item dev">
          <div class="when">2023 — Present</div>
          <h3>Freelance Web Developer</h3>
          <div class="org">Independent</div>
          <ul>
            <li>Design and build responsive websites for individuals and small businesses</li>
            <li>Translate simple briefs into clean, fast, mobile-friendly pages</li>
            <li>Handle everything end-to-end — structure, styling and basic interactivity</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section id="education">
    <div class="wrap">
      <div class="section-head reveal">
        <div class="eyebrow">Education</div>
        <h2>Academic background.</h2>
      </div>
      <div class="edu-grid">
        <div class="edu-card reveal"><div class="year">2023</div><h3>Higher Secondary (12th — Science)</h3><p>Anuj Convent Hr. Sec. School, Gwalior</p></div>
        <div class="edu-card reveal"><div class="year">2021</div><h3>10th Standard</h3><p>Well Founded Hr. Sec. School, Gwalior</p></div>
      </div>
    </div>
  </section>

  <section id="about-cta">
    <div class="wrap">
      <div class="cta-strip reveal">
        <h2>Want the full picture?</h2>
        <p>Reach out for my resume, references, or to talk about a role or project.</p>
        <a href="contact.html" class="btn btn-primary">Contact me →</a>
      </div>
    </div>
  </section>'''
page("about.html", "About — Aditya Tomar",
     "About Aditya Tomar — HR Executive and freelance web developer based in Surat, Gujarat.",
     about_body, "about.html")


# ============ SERVICES ============
services = [
    ("Landing Pages & Small Business Sites", "Clean, fast, mobile-first websites for local businesses, personal brands and portfolios — built and handed over end-to-end.", ["HTML/CSS/JS","Responsive","SEO basics"]),
    ("Portfolio & Personal Websites", "A polished single-page or multi-page portfolio like this one — with animations, dark mode and a contact form.", ["Animations","Dark mode","Contact form"]),
    ("Website Redesign & Revamp", "Already have a site that feels dated? I'll modernise the layout, speed and responsiveness.", ["Redesign","Performance","Mobile-first"]),
    ("HR Consulting (Freelance)", "Help with payroll structuring, attendance systems, PF/ESIC compliance basics and HR documentation for small teams.", ["Payroll","Compliance","HR docs"]),
    ("AI-Assisted Builds", "Faster delivery by combining hand-written code with modern AI tooling — without cutting corners on quality.", ["AI tools","Fast delivery","Clean code"]),
    ("Maintenance & Small Edits", "Ongoing tweaks, content updates and small fixes so your site stays fresh after launch.", ["Updates","Fixes","Support"]),
]
svc_cards = ""
for t, d, tags in services:
    stack = "".join(f"<span>{x}</span>" for x in tags)
    svc_cards += f'''<div class="work-card reveal">
        <div class="tagrow"><span class="kind">Service</span></div>
        <h3>{t}</h3>
        <p>{d}</p>
        <div class="stack">{stack}</div>
        <a href="contact.html" class="go">Enquire →</a>
      </div>'''
services_body = f'''  <section class="page-pad" id="services">
    <div class="wrap">
      <div class="section-head reveal">
        <div class="eyebrow">Services</div>
        <h2>How I can help.</h2>
        <p>I'm early in my freelance journey and take on a limited number of builds alongside my HR role — here's what I offer.</p>
      </div>
      <div class="work-grid">
        {svc_cards}
      </div>
    </div>
  </section>

  <section id="process">
    <div class="wrap">
      <div class="section-head reveal">
        <div class="eyebrow">Process</div>
        <h2>Simple, transparent steps.</h2>
      </div>
      <div class="timeline reveal">
        <div class="tl-item"><div class="when">Step 01</div><h3>Brief & Quote</h3><div class="org">Free</div><ul><li>You share what you need; I send a clear scope and a fair, fixed price.</li></ul></div>
        <div class="tl-item dev"><div class="when">Step 02</div><h3>Design & Build</h3><div class="org">Hands-on</div><ul><li>I design and code a responsive layout, sharing progress along the way.</li></ul></div>
        <div class="tl-item"><div class="when">Step 03</div><h3>Review & Revisions</h3><div class="org">Collaborative</div><ul><li>You review, we refine — small revisions are part of the deal.</li></ul></div>
        <div class="tl-item dev"><div class="when">Step 04</div><h3>Launch & Handover</h3><div class="org">Done</div><ul><li>Files handed over, deployed if needed, with optional ongoing support.</li></ul></div>
      </div>
    </div>
  </section>

  <section id="services-cta">
    <div class="wrap">
      <div class="cta-strip reveal">
        <h2>Have a website in mind?</h2>
        <p>Tell me about your project and I'll get back to you quickly with a plan and a quote.</p>
        <a href="contact.html" class="btn btn-primary">Start a project →</a>
      </div>
    </div>
  </section>'''
page("services.html", "Services — Aditya Tomar",
     "Freelance web development and HR consulting services by Aditya Tomar.",
     services_body, "services.html")


# ============ PROJECTS / GITHUB ============
# Categories: own first, then Java, React, Full Stack, Data Science, C++, Machine Learning
projects = [
    # Own / free starter projects (front-end, beginner friendly, free to clone)
    ("Own", "Personal Portfolio Template", "A clean, animated, dark-mode portfolio template built with plain HTML, CSS & JS — free to clone and customise.", "https://github.com/topics/portfolio-template", True),
    ("Own", "Responsive Landing Page Kit", "Modern, mobile-first landing page sections you can mix and match for any small business.", "https://github.com/topics/landing-page", True),
    ("Own", "JavaScript To-Do App", "A simple, dependency-free to-do list with local storage — great starter project.", "https://github.com/topics/todo-list", True),
    ("Own", "Calculator (HTML/CSS/JS)", "A responsive calculator with keyboard support — pure vanilla JavaScript.", "https://github.com/topics/calculator-javascript", True),
    ("Own", "Weather App (API)", "Fetches live weather from a public API and displays it in a clean card UI.", "https://github.com/topics/weather-app", True),
    ("Own", "Quiz App (Vanilla JS)", "A timed multiple-choice quiz app with score tracking, no frameworks needed.", "https://github.com/topics/quiz-app", True),

    # JAVA
    ("Java", "Password Generator using Java", "Generate strong, random passwords with configurable rules.", "https://github.com/KZarzour/Password-Generator", False),
    ("Java", "Online Survey System", "Create and run online surveys, collect and view responses.", "https://github.com/kodekracker/Online-Survey-System", False),
    ("Java", "Online Resume Builder", "Build and export professional resumes from a web form.", "https://github.com/meetakbari/CV-Resume-Builder", False),
    ("Java", "Snake Game using Java", "The classic snake game built with Java Swing.", "https://github.com/janbodnar/Java-Snake-Game", False),
    ("Java", "Data Visualization Software", "GROOT — a data visualization toolkit for scientific data.", "https://github.com/gavalian/groot", False),
    ("Java", "Electricity Billing System", "Manage customers and generate electricity bills.", "https://github.com/Adarsh9616/Electricity_Billing_System", False),
    ("Java", "Web Medical Management System", "A medical center management web application.", "https://github.com/mokarrom/medical-center", False),
    ("Java", "Supply Chain Management System", "Backend for a supply chain management platform.", "https://github.com/sonnyhcl/Backend", False),
    ("Java", "Exam Seating Arrangement System", "Automate exam seating using JSP & Servlets.", "https://github.com/chabedalam11/Exam-Seating-Arrangement-System-Using-JSP-Servlet", False),
    ("Java", "Wordcount Tools in Java", "A command-line word counting utility.", "https://github.com/lucassrg/javawc", False),
    ("Java", "Consumer Relationship Management", "A CRM system for managing customer relationships.", "https://github.com/machowina/CRM", False),
    ("Java", "bFit Cognitive & Memory Game", "A cognitive and memory testing game.", "https://github.com/Dk35840/bFit-A-Cognitive-Game", False),
    ("Java", "Network Packet Sniffer Analyzer", "Capture and analyse network packets.", "https://github.com/HassanAdamm/packet-sniffer", False),
    ("Java", "ISP Automation System", "Automation system for internet service providers.", "https://github.com/nitishr7/ISP-Java", False),
    ("Java", "Criminal Face Detection System", "Face recognition for identifying individuals.", "https://github.com/prasadus92/Face-Recognition", False),

    # React
    ("React", "React Notes Application", "A simple notes app built with React.", "https://github.com/paydendyer/react-notes-app", False),
    ("React", "React Pokemon App (PokeAPI)", "Browse Pokémon using the public PokeAPI.", "https://github.com/Megh2507/Pokemon-App", False),
    ("React", "React Weather Application", "Live weather app built with React.", "https://github.com/topics/react-weather-app", False),
    ("React", "React Cryptocurrency App", "Track cryptocurrency prices in real time.", "https://github.com/Megh2507/React-Crypto-App", False),
    ("React", "React Password Generator", "Generate secure passwords with React.", "https://github.com/Megh2507/react_password_generator", False),
    ("React", "Photo Gallery Application", "A full-stack photo gallery with React & Node.", "https://github.com/chrisblakely01/react-node-photo-gallery", False),
    ("React", "React Chat Application", "A WhatsApp-style chat clone.", "https://github.com/WebDevSimplified/Whatsapp-Clone", False),
    ("React", "React Movie & Series App", "An entertainment hub for movies and series.", "https://github.com/piyush-eon/react-entertainment-hub", False),
    ("React", "Instagram Clone", "Instagram clone projects collection.", "https://github.com/topics/instagram-clone", False),
    ("React", "E-Commerce Application", "A MERN-stack e-commerce application.", "https://github.com/meabhisingh/mernProjectEcommerce", False),

    # Full Stack
    ("Full Stack", "To-do List Project", "A full-stack Node.js to-do application.", "https://github.com/snyk-labs/nodejs-goof", False),
    ("Full Stack", "Blog Website / App", "A React + Redux blog platform.", "https://github.com/rajaraodv/react-redux-blog", False),
    ("Full Stack", "Chat Application / Website", "Realtime chat with React, Redux & Socket.IO.", "https://github.com/raineroviir/react-redux-socketio-chat", False),
    ("Full Stack", "Portfolio Website", "A full portfolio website project.", "https://github.com/adrianhajdin/portfolio_website", False),
    ("Full Stack", "Food Delivery App / Website", "A quick food delivery website in React.", "https://github.com/fahadahmed07/react-js-quick-food-delivery-website", False),
    ("Full Stack", "E-commerce Website / App", "Django Oscar — a robust e-commerce framework.", "https://github.com/django-oscar/django-oscar", False),
    ("Full Stack", "Video Conferencing App", "A video chat app/website.", "https://github.com/itstaranarora/video-chat-v1", False),
    ("Full Stack", "Social Media App / Website", "A social media application.", "https://github.com/CharlyKeleb/SocialMedia-App", False),
    ("Full Stack", "CMS for Blogs", "A content management system for blogs.", "https://github.com/mahmudahsan/pythonbangla.com", False),
    ("Full Stack", "Project Management Tool", "Taskcafe — an open-source project management tool.", "https://github.com/JordanKnott/taskcafe", False),

    # Data Science
    ("Data Science", "Fake News Detection (Python)", "Detect fake news using machine learning.", "https://github.com/nishitpatel01/Fake_News_Detection", False),
    ("Data Science", "Detecting Forest Fire", "Fire detection from imagery.", "https://github.com/Skar0/fire-detection", False),
    ("Data Science", "Road Lane Line Detection", "An awesome list of lane detection resources.", "https://github.com/amusi/awesome-lane-detection", False),
    ("Data Science", "Sentiment Analysis", "ML-based sentiment analysis.", "https://github.com/yashspr/sentiment_analysis_ml_part", False),
    ("Data Science", "Speech Emotion Recognition", "Recognise emotions from speech.", "https://github.com/topics/speech-emotion-recognition", False),
    ("Data Science", "Gender & Age Detection", "Predict gender and age from images.", "https://github.com/smahesh29/Gender-and-Age-Detection", False),
    ("Data Science", "Developing Chatbots", "Build a simple chatbot in Python with NLTK.", "https://github.com/parulnith/Building-a-Simple-Chatbot-in-Python-using-NLTK", False),
    ("Data Science", "Diabetic Retinopathy Detection", "Detect diabetic retinopathy from scans.", "https://github.com/rsk97/Diabetic-Retinopathy-Detection", False),
    ("Data Science", "Credit Card Fraud Detection", "Detect fraud using autoencoders in Keras.", "https://github.com/curiousily/Credit-Card-Fraud-Detection-using-Autoencoders-in-Keras", False),
    ("Data Science", "Web Scraper", "Reusable web scraping functions.", "https://github.com/madhurimarawat/Web-Scrapper-Functions", False),

    # C++
    ("C++", "Bookshop Management System", "Manage a bookshop's inventory and sales.", "https://github.com/aryan-khanijo/Bookshop-Management-System-CPP-Project", False),
    ("C++", "Bank Management System", "A C++ bank management system.", "https://github.com/wkhaliddev/Bank-Management/tree/master/DSAproject", False),
    ("C++", "Student Record Management", "Manage student records in C++.", "https://github.com/Code-Recursion/Student-Record-Management-System", False),
    ("C++", "Contact Management System", "Store and manage contacts.", "https://github.com/JeremyWu917/ContactManagementSystem", False),
    ("C++", "Car Rental System", "A car rental management system.", "https://github.com/Ellie-Y/CarRentalSystem", False),
    ("C++", "Credit Card Validator", "Validate credit card numbers.", "https://github.com/karancodes/credit-card-validator", False),
    ("C++", "Sudoku Game", "Play and solve Sudoku.", "https://github.com/AlexIzydorczyk/sudoku", False),
    ("C++", "Trading Application", "Qt Bitcoin Trader.", "https://github.com/JulyIghor/QtBitcoinTrader", False),
    ("C++", "Casino Number Guessing Game", "A baccarat casino number game.", "https://github.com/KevinVillania/Baccarat-Casino-Number-Game", False),
    ("C++", "Sales Management System", "Manage sales records.", "https://github.com/whoeverxd/sales", False),
    ("C++", "Face Detection App with C++", "Feature & face detection.", "https://github.com/elador/FeatureDetection", False),
    ("C++", "Digital Calculator", "A C++ calculator.", "https://github.com/christopher-siewert/cpp-calculator", False),

    # Machine Learning
    ("Machine Learning", "Home Value Prediction", "Predict house prices with ML.", "https://github.com/Shreyas3108/house-price-prediction", False),
    ("Machine Learning", "Sales Prediction Project", "Predict future sales (Kaggle).", "https://github.com/storieswithsiva/Kaggle-Predicting-Future-Sales", False),
    ("Machine Learning", "Music Recommendation System", "Recommend music to users.", "https://github.com/ugis22/music_recommender", False),
    ("Machine Learning", "Black Friday Sales Prediction", "Predict Black Friday sales.", "https://github.com/nanthasnk/Black-Friday-Sales-Prediction", False),
    ("Machine Learning", "Stock Price Predictor", "Time-series stock prediction models.", "https://github.com/huseinzol05/Stock-Prediction-Models", False),
    ("Machine Learning", "Wine Quality Prediction", "Predict wine quality from data.", "https://github.com/amberkakkar01/Prediction-of-Wine-Quality", False),
    ("Machine Learning", "MNIST Digit Classification", "Handwritten digit recognition.", "https://github.com/anujdutt9/Handwritten-Digit-Recognition-using-Deep-Learning", False),
    ("Machine Learning", "Market Basket Analysis", "Find product associations.", "https://github.com/DiegoUsaiUK/Market_Basket_Analysis", False),
    ("Machine Learning", "Text Summarisation", "Summarise text automatically.", "https://github.com/ebenso/TextSummarizer", False),
    ("Machine Learning", "HypertuneML", "ML model datasets using Streamlit.", "https://github.com/madhurimarawat/ML-Model-Datasets-Using-Streamlits", False),
]

cats = ["All", "Own", "Java", "React", "Full Stack", "Data Science", "C++", "Machine Learning"]
filter_btns = ""
for c in cats:
    active = ' active' if c == "All" else ''
    filter_btns += f'<button class="filter-btn{active}" data-filter="{html.escape(c)}">{html.escape(c)}</button>'

gh_icon = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 .5A11.5 11.5 0 0 0 .5 12a11.5 11.5 0 0 0 7.86 10.92c.575.106.785-.25.785-.555 0-.274-.01-1-.015-1.965-3.196.695-3.87-1.54-3.87-1.54-.523-1.33-1.278-1.685-1.278-1.685-1.044-.714.08-.7.08-.7 1.155.082 1.763 1.186 1.763 1.186 1.026 1.758 2.693 1.25 3.35.955.104-.743.402-1.25.73-1.538-2.552-.29-5.236-1.276-5.236-5.68 0-1.255.448-2.28 1.183-3.084-.119-.29-.513-1.46.112-3.044 0 0 .966-.31 3.166 1.178a10.98 10.98 0 0 1 2.882-.388c.978.004 1.963.132 2.883.388 2.198-1.488 3.163-1.178 3.163-1.178.626 1.584.232 2.754.114 3.044.737.804 1.182 1.829 1.182 3.084 0 4.415-2.688 5.387-5.248 5.671.413.355.78 1.057.78 2.13 0 1.538-.014 2.778-.014 3.157 0 .308.207.667.79.554A11.5 11.5 0 0 0 23.5 12 11.5 11.5 0 0 0 12 .5z"/></svg>'

proj_cards = ""
for cat, title, desc, url, own in projects:
    search = f"{title} {desc} {cat}"
    badge = '<span class="proj-badge-own">Free starter</span>' if own else f'<span class="proj-cat">{html.escape(cat)}</span>'
    proj_cards += f'''<div class="proj-card reveal" data-cat="{html.escape(cat)}" data-search="{html.escape(search)}">
        <div class="proj-top"><span class="proj-cat">{html.escape(cat)}</span>{'<span class="proj-badge-own">Free starter</span>' if own else ''}</div>
        <h3>{html.escape(title)}</h3>
        <p>{html.escape(desc)}</p>
        <a class="proj-link" href="{html.escape(url)}" target="_blank" rel="noopener noreferrer">{gh_icon} View Source Code →</a>
      </div>'''

projects_body = f'''  <section class="page-pad" id="projects">
    <div class="wrap">
      <div class="section-head reveal">
        <div class="eyebrow">GitHub · Source Code Library</div>
        <h2>Explore the code.</h2>
        <p>A curated library of projects bundled with their source code — plus free starter projects you can clone and customise. Click any card to jump straight to its GitHub repository.</p>
      </div>
      <div class="reveal" style="margin-bottom:26px;">
        <div class="field" style="max-width:420px;margin-bottom:22px;">
          <input id="projSearch" type="text" placeholder="Search projects…" aria-label="Search projects">
        </div>
        <div class="filter-bar" id="filterBar">{filter_btns}</div>
        <div class="proj-count" id="projCount"></div>
      </div>
      <div class="proj-grid">
        {proj_cards}
      </div>
      <div class="no-results" id="noResults" style="display:none;">No projects match your search.</div>
    </div>
  </section>

  <section id="contribute">
    <div class="wrap">
      <div class="cta-strip reveal">
        <h2>Want a custom build?</h2>
        <p>Like one of these and want your own version, or something new entirely? I build clean, responsive sites and apps — let's talk.</p>
        <a href="contact.html" class="btn btn-primary">Start a project →</a>
      </div>
    </div>
  </section>'''
page("projects.html", "GitHub — Source Code Library | Aditya Tomar",
     "A curated library of source-code projects across Java, React, Full Stack, Data Science, C++ and Machine Learning, plus free starter projects.",
     projects_body, "projects.html")


# ============ CONTACT ============
contact_body = f'''  <section class="page-pad" id="contact">
    <div class="wrap">
      <div class="section-head reveal">
        <div class="eyebrow">Contact</div>
        <h2>Let's build something.</h2>
        <p>Open to HR roles, freelance web projects, or just a conversation — drop a message, I reply quickly.</p>
      </div>
      <div class="contact-grid">
        <div class="contact-info reveal">
          <p>The fastest way to reach me is email. Use the form and it'll open your email app pre-filled, or contact me directly through any of the channels below.</p>
          <div class="info-list">
            <div class="row">
              <span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg></span>
              <span><span class="lab">Email</span><br><span class="val">{EMAIL}</span></span>
            </div>
            <div class="row">
              <span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M21 10c0 7-9 12-9 12s-9-5-9-12a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>
              <span><span class="lab">Location</span><br><span class="val">Surat, Gujarat, India</span></span>
            </div>
            <div class="row">
              <span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.5 3.5 6 3.5 9s-1 6.5-3.5 9c-2.5-2.5-3.5-6-3.5-9s1-6.5 3.5-9z"/></svg></span>
              <span><span class="lab">Open to</span><br><span class="val">HR roles (India / Gulf / Europe) & freelance builds</span></span>
            </div>
          </div>
          <div class="social-row" style="justify-content:flex-start;margin-top:28px;">
            <a href="mailto:{EMAIL}" aria-label="Email" title="Email"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg></a>
            <a href="#" aria-label="LinkedIn" title="LinkedIn (add your URL)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M7 10v7M7 7v.01M11 17v-4.5a2 2 0 0 1 4 0V17M11 12.5V17"/></svg></a>
            <a href="{GITHUB}" target="_blank" rel="noopener noreferrer" aria-label="GitHub" title="GitHub (add your username)"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 .5A11.5 11.5 0 0 0 .5 12a11.5 11.5 0 0 0 7.86 10.92c.575.106.785-.25.785-.555 0-.274-.01-1-.015-1.965-3.196.695-3.87-1.54-3.87-1.54-.523-1.33-1.278-1.685-1.278-1.685-1.044-.714.08-.7.08-.7 1.155.082 1.763 1.186 1.763 1.186 1.026 1.758 2.693 1.25 3.35.955.104-.743.402-1.25.73-1.538-2.552-.29-5.236-1.276-5.236-5.68 0-1.255.448-2.28 1.183-3.084-.119-.29-.513-1.46.112-3.044 0 0 .966-.31 3.166 1.178a10.98 10.98 0 0 1 2.882-.388c.978.004 1.963.132 2.883.388 2.198-1.488 3.163-1.178 3.163-1.178.626 1.584.232 2.754.114 3.044.737.804 1.182 1.829 1.182 3.084 0 4.415-2.688 5.387-5.248 5.671.413.355.78 1.057.78 2.13 0 1.538-.014 2.778-.014 3.157 0 .308.207.667.79.554A11.5 11.5 0 0 0 23.5 12 11.5 11.5 0 0 0 12 .5z"/></svg></a>
          </div>
        </div>

        <form class="form-card reveal" id="contactForm">
          <div class="field"><label for="name">Your name</label><input id="name" name="name" type="text" required placeholder="Jane Doe"></div>
          <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" required placeholder="jane@example.com"></div>
          <div class="field"><label for="message">Message</label><textarea id="message" name="message" required placeholder="Tell me about your project or role…"></textarea></div>
          <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center;">Send message →</button>
          <p class="form-note" id="formStatus">This opens your email app with the message pre-filled.</p>
        </form>
      </div>
    </div>
  </section>'''
page("contact.html", "Contact — Aditya Tomar",
     "Get in touch with Aditya Tomar for HR roles, freelance web projects or collaboration.",
     contact_body, "contact.html")


# ============ TERMS ============
terms_body = '''  <section class="page-pad" id="terms">
    <div class="wrap">
      <div class="section-head reveal">
        <div class="eyebrow">Legal</div>
        <h2>Terms &amp; Conditions</h2>
      </div>
      <div class="prose reveal">
        <p class="updated">Last updated: 29 June 2026</p>
        <p>Welcome to the personal portfolio website of <strong>Aditya Tomar</strong> ("the Site"). By accessing or using this Site, you agree to be bound by these Terms &amp; Conditions. If you do not agree, please do not use the Site.</p>

        <h2>1. Use of the Site</h2>
        <p>This Site is provided for informational and portfolio purposes. You may browse and share its content for personal, non-commercial use. You agree not to misuse the Site, attempt to disrupt it, or use it for any unlawful purpose.</p>

        <h2>2. Intellectual Property</h2>
        <p>The design, text, graphics and original code of this Site are owned by Aditya Tomar unless stated otherwise. You may not copy, reproduce or redistribute the Site's original content without permission.</p>

        <h2>3. Third-Party Links &amp; Source Code Library</h2>
        <p>The "GitHub / Source Code Library" page links to third-party repositories hosted on GitHub and other platforms. These projects are the property of their respective authors and are governed by their own licenses. Aditya Tomar does not own these repositories, makes no warranty about them, and is not responsible for their content, availability or licensing. Always review each repository's license before use.</p>

        <h2>4. Freelance Services</h2>
        <p>Any freelance development or consulting work is subject to a separate agreement (scope, timeline and price) confirmed in writing before work begins. Quotes shared on this Site are indicative only.</p>

        <h2>5. Disclaimer</h2>
        <p>The Site and its content are provided "as is" without warranties of any kind. While I aim for accuracy, I do not guarantee that the Site will be error-free or continuously available.</p>

        <h2>6. Limitation of Liability</h2>
        <p>To the maximum extent permitted by law, Aditya Tomar shall not be liable for any direct, indirect or consequential loss arising from your use of, or inability to use, this Site or any linked third-party resource.</p>

        <h2>7. Changes to These Terms</h2>
        <p>These Terms may be updated from time to time. Continued use of the Site after changes means you accept the revised Terms.</p>

        <h2>8. Contact</h2>
        <p>Questions about these Terms? Email <a href="mailto:''' + EMAIL + '''">''' + EMAIL + '''</a>.</p>
      </div>
    </div>
  </section>'''
page("terms.html", "Terms & Conditions — Aditya Tomar",
     "Terms and conditions for Aditya Tomar's portfolio website.",
     terms_body, "terms.html")


# ============ PRIVACY ============
privacy_body = '''  <section class="page-pad" id="privacy">
    <div class="wrap">
      <div class="section-head reveal">
        <div class="eyebrow">Legal</div>
        <h2>Privacy Policy</h2>
      </div>
      <div class="prose reveal">
        <p class="updated">Last updated: 29 June 2026</p>
        <p>This Privacy Policy explains how <strong>Aditya Tomar</strong> ("I", "me") handles information when you use this portfolio website.</p>

        <h2>1. Information I Collect</h2>
        <p>This Site is a static portfolio and does not run hidden tracking. Information is only collected when you choose to provide it:</p>
        <ul>
          <li><strong>Contact form:</strong> Your name, email and message. The form opens your own email app to send the message directly to me — the data is not stored on a server by this Site.</li>
          <li><strong>Theme preference:</strong> Your light/dark mode choice is saved locally in your browser (localStorage) for your convenience. It never leaves your device.</li>
        </ul>

        <h2>2. How I Use Your Information</h2>
        <p>Any details you send by email are used solely to respond to your enquiry about HR roles, freelance projects or collaboration. I do not sell or share your information.</p>

        <h2>3. Cookies &amp; Local Storage</h2>
        <p>This Site does not use advertising or tracking cookies. It uses your browser's local storage only to remember your theme preference. You can clear this at any time in your browser settings.</p>

        <h2>4. Third-Party Services</h2>
        <p>Some pages load fonts from Google Fonts and link out to GitHub repositories. When you visit those external sites, their own privacy policies apply.</p>

        <h2>5. Data Security</h2>
        <p>Because this Site does not collect or store personal data on a server, the main safeguard is your own email communication. I treat any information you send me with care and confidentiality.</p>

        <h2>6. Your Rights</h2>
        <p>You may ask me to delete any email correspondence you've sent, or to stop contacting you, at any time. Just email me.</p>

        <h2>7. Contact</h2>
        <p>Questions about privacy? Email <a href="mailto:''' + EMAIL + '''">''' + EMAIL + '''</a>.</p>
      </div>
    </div>
  </section>'''
page("privacy.html", "Privacy Policy — Aditya Tomar",
     "Privacy policy for Aditya Tomar's portfolio website.",
     privacy_body, "privacy.html")

print("Done.")
