<!-- PROJECT BANNER -->
<div align="center">

# 🌌 Aditya Tomar — Portfolio Website

### HR Executive × Freelance Web Developer

A modern, animated, fully responsive **multi-page portfolio** built with plain
**HTML, CSS & JavaScript** — featuring a dark/light theme toggle, particle
background, custom cursor, scroll animations, and a curated **GitHub Source-Code
Library**.

<!-- BADGES -->
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![No Dependencies](https://img.shields.io/badge/Dependencies-0-brightgreen?style=for-the-badge)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)

[**🔗 Live Demo**](https://tomar760.github.io/portfolio/) &nbsp;·&nbsp;
[**📂 Projects Library**](https://tomar760.github.io/portfolio/projects.html) &nbsp;·&nbsp;
[**✉️ Contact**](mailto:tomaraditya760@gmail.com)

</div>

---

## 📖 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Pages](#-pages)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Editing & Rebuilding](#-editing--rebuilding)
- [Deployment (GitHub Pages)](#-deployment-github-pages)
- [Customisation Checklist](#-customisation-checklist)
- [Screenshots](#-screenshots)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🧭 About

This is the personal portfolio of **Aditya Tomar**, an HR Executive based in
Surat, Gujarat, India, who also works as a freelance web developer. The site
showcases experience, skills, services, and a large, filterable library of
open-source project ideas (each linking straight to its GitHub repository).

The whole site is **static** — no frameworks, no build tools required to run it.
A small optional Python script regenerates the pages from shared templates.

---

## ✨ Features

| | Feature | Description |
|---|---|---|
| 🌙 | **Dark / Light mode** | Dark by default, with a toggle. Preference is saved in `localStorage`. |
| 🎇 | **Particle network** | Animated canvas background that adapts to the theme. |
| 🖱️ | **Custom cursor** | Glow + ring cursor on desktop (auto-disabled on touch / reduced-motion). |
| 📜 | **Scroll reveal** | Sections fade and slide in as you scroll. |
| 🃏 | **3D tilt cards** | Cards subtly tilt towards the mouse. |
| ⌨️ | **Typing effect** | Animated "currently into…" text in the hero. |
| 🔢 | **Count-up stats** | Animated numbers in the hero. |
| 🗂️ | **Projects library** | 70+ projects with **category filters** + **live search**. |
| 📱 | **Fully responsive** | Mobile-first, with an animated hamburger menu. |
| ♿ | **Accessible** | Respects `prefers-reduced-motion`, semantic markup, keyboard-friendly. |
| 📨 | **Contact form** | Opens the visitor's email app pre-filled (no backend needed). |
| ⚖️ | **Legal pages** | Terms & Conditions + Privacy Policy included. |

---

## 🛠 Tech Stack

- **HTML5** — semantic, multi-page
- **CSS3** — custom properties (theming), grid/flex, animations, no framework
- **Vanilla JavaScript (ES6+)** — no libraries, no dependencies
- **Python 3** *(optional)* — `build.py` regenerates pages from shared templates

> **Zero runtime dependencies.** The site runs by simply opening the HTML files.

---

## 📄 Pages

| Page | File | Purpose |
|---|---|---|
| 🏠 Home | `index.html` | Hero, snapshot, skills, call-to-action |
| 👤 About | `about.html` | Bio, experience timeline, education |
| 🧰 Services | `services.html` | Service offerings + work process |
| 💻 GitHub | `projects.html` | Filterable source-code library (70+ projects) |
| ✉️ Contact | `contact.html` | Contact form + details |
| 📜 Terms | `terms.html` | Terms & Conditions |
| 🔒 Privacy | `privacy.html` | Privacy Policy |

---

## 🗂 Project Structure

```text
portfolio/
├── index.html              # Home
├── about.html              # About + experience + education
├── services.html           # Services + process
├── projects.html           # GitHub source-code library
├── contact.html            # Contact form
├── terms.html              # Terms & Conditions
├── privacy.html            # Privacy Policy
│
├── assets/
│   ├── theme.css           # Shared styles (dark/light tokens, components)
│   └── app.js              # Shared scripts (theme, animations, filters)
│
├── build.py                # Optional generator → rebuilds all .html pages
│
├── .github/
│   └── workflows/
│       └── deploy.yml      # Auto-deploy to GitHub Pages
│
├── .gitignore
├── LICENSE                 # MIT
├── CONTRIBUTING.md
└── README.md               # You are here
```

> **Note:** `theme.css` and `app.js` are the single source of truth for styling
> and behaviour. `build.py` **inlines** them into every page so the site works
> even when opened directly from disk (no server required).

---

## 🚀 Getting Started

### Option 1 — Just open it
```bash
git clone https://github.com/tomar760/portfolio.git
cd portfolio
# Open index.html in your browser
```

### Option 2 — Run a local server (recommended)
```bash
# Python 3
python3 -m http.server 8000
# then visit http://localhost:8000
```

```bash
# or with Node
npx serve .
```

---

## ✏️ Editing & Rebuilding

You can edit the `.html` files directly — but the cleanest way is to edit the
shared templates and regenerate everything:

1. Edit content/styles/scripts in **`build.py`**, **`assets/theme.css`**, or **`assets/app.js`**.
2. Rebuild all pages:
   ```bash
   python3 build.py
   ```
3. The script rewrites every `*.html` with the updated shared shell.

**Add a project to the library:** open `build.py`, find the `projects = [ ... ]`
list and add a tuple:
```python
("React", "Project Title", "Short description.", "https://github.com/user/repo", False),
#  ^category  ^title          ^description          ^GitHub URL                     ^is "free starter"?
```
Then run `python3 build.py`.

---

## 🌐 Deployment (GitHub Pages)

This repo ships with an automated workflow at
`.github/workflows/deploy.yml`. To go live:

1. Push the repo to GitHub.
2. Go to **Settings → Pages → Build and deployment → Source → GitHub Actions**.
3. Push to `main` — the site deploys automatically.
4. Your site will be at `https://tomar760.github.io/portfolio/`.

> Prefer the simple way? **Settings → Pages → Deploy from a branch → `main` / root.**

---

## ✅ Customisation Checklist

Before going live, update these placeholders:

- [x] Replace `YOUR-USERNAME` in this README's links and badges (set to `tomar760`)
- [x] Add your **GitHub** profile URL (set to https://github.com/tomar760)
- [ ] Add your **LinkedIn** URL (currently `#` on the contact page)
- [ ] Add a **resume** file and link the "Download Resume" button
- [ ] Update the email if it changes (`tomaraditya760@gmail.com`)
- [ ] Add real **screenshots** to the section below
- [ ] (Optional) Add a custom domain via a `CNAME` file

After any change in `build.py`/`assets`, run `python3 build.py`.

---

## 🖼 Screenshots

> Add screenshots/GIFs here once deployed. Suggested:

| Home (Dark) | Projects Library | Light Mode |
|---|---|---|
| _add image_ | _add image_ | _add image_ |

```markdown
<!-- Example -->
![Home page](docs/screenshot-home.png)
```

---

## 🗺 Roadmap

- [ ] Add real freelance project case studies
- [ ] Blog section
- [ ] Downloadable resume (PDF)
- [ ] Open Graph / social preview images
- [ ] Contact form backend (e.g. Formspree) as an alternative to `mailto:`

---

## 🤝 Contributing

Contributions, suggestions and bug reports are welcome!
See **[CONTRIBUTING.md](CONTRIBUTING.md)** for guidelines.

1. Fork the repo
2. Create a branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## ⚖️ License

This project's **original code** is released under the **MIT License** — see
[LICENSE](LICENSE).

> The projects listed in the **Source-Code Library** (`projects.html`) link to
> third-party repositories owned by their respective authors and are governed by
> their own licenses. Please review each repository's license before use.

---

## 📬 Contact

**Aditya Tomar** — HR Executive & Freelance Web Developer
📍 Surat, Gujarat, India

[![Email](https://img.shields.io/badge/Email-tomaraditya760@gmail.com-D14836?style=flat&logo=gmail&logoColor=white)](mailto:tomaraditya760@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin&logoColor=white)](#)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat&logo=github&logoColor=white)](https://github.com/tomar760)

---

<div align="center">

⭐ **If you like this project, consider giving it a star!** ⭐

Made with care by Aditya Tomar · © 2026

</div>
