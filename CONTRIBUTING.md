# Contributing Guide

Thanks for your interest in improving this portfolio project! 🎉
Contributions of all sizes are welcome — fixes, new project entries, design
tweaks, accessibility improvements, and documentation.

## 🧰 Before You Start

This is a **dependency-free static site**:

- `assets/theme.css` → all styling (dark/light theme tokens, components)
- `assets/app.js` → all behaviour (theme toggle, animations, filters)
- `build.py` → optional generator that **inlines** the CSS/JS into each `.html`

Edit the shared files, then run the generator so every page stays in sync.

## 🚀 Local Setup

```bash
# 1. Fork & clone
git clone https://github.com/YOUR-USERNAME/portfolio.git
cd portfolio

# 2. Serve locally
python3 -m http.server 8000
# visit http://localhost:8000

# 3. After editing build.py / assets, regenerate pages
python3 build.py
```

## 🌿 Branch & Commit

1. Create a descriptive branch:
   ```bash
   git checkout -b feature/add-vue-projects
   ```
2. Use clear, conventional commit messages, e.g.:
   - `feat: add Vue.js category to projects library`
   - `fix: correct mobile nav z-index`
   - `docs: update customisation checklist`
   - `style: tweak card hover shadow`

## ➕ Adding a Project to the Library

Open `build.py`, find the `projects = [ ... ]` list, and add a tuple:

```python
("Category", "Project Title", "One-line description.", "https://github.com/user/repo", False)
```

- **Category** must be one of the existing ones (or add it to the `cats` list too).
- The last value is `True` only for your own "free starter" projects.
- Run `python3 build.py` and confirm the card appears and filters correctly.

## ✅ Pull Request Checklist

Before opening a PR, please make sure:

- [ ] `python3 build.py` runs without errors
- [ ] All pages open correctly in the browser
- [ ] Dark **and** light mode both look correct
- [ ] Layout works on mobile (≤ 480px) and desktop
- [ ] No new external dependencies were added
- [ ] Links open correctly (external links use `target="_blank"`)

## 🐞 Reporting Bugs

Open an issue with:

- What you expected vs. what happened
- Steps to reproduce
- Browser & device
- A screenshot if it's visual

## 📜 Code of Conduct

Be respectful and constructive. We want this to be a welcoming space for
contributors of every experience level.

---

Thank you for contributing! 💜
