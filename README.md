# Amit Das — Portfolio

Personal portfolio site for **Amit Das** — AI Director & Creative Director
(luxury, jewellery & fashion), grounded in thirteen years of filmmaking,
cinematography and post.

Built as a small **Flask** app with the frontend styled in **Tailwind CSS**.
All page content lives in `content.py`, rendered through Jinja2 templates.

## Stack & layout

```
app.py                 Flask app — GET / and GET /work/<slug>
content.py             All page copy as Python data (edit the site here)
templates/
  base.html            <head>, nav, atmosphere layers, footer, scripts
  index.html           The full home page, rendered from content.py
  section.html         A focused, shareable page per work vertical
  _card.html           Work-card macro (shared)
  _contact.html        Contact block — email + socials (shared)
src/input.css          Tailwind entry + custom cinema-effect layer
tailwind.config.js     Design tokens (palette, fonts, type scale, animations)
static/css/tailwind.css  Built stylesheet (generated; committed so it runs w/o Node)
static/img/work/       Work thumbnails (see that folder's README)
```

## Run locally

Two toolchains: Node builds the CSS, Python runs the site.

```bash
# 1. Build the stylesheet (only needed once, or after editing styles/templates)
npm install
npm run build:css

# 2. Run the app
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
flask run            # or: python app.py
```

Open <http://localhost:5000>. While editing styles, run `npm run watch:css` in a
second terminal to rebuild `static/css/tailwind.css` automatically.

## Contact

Contact is a plain `mailto:` link plus social links (set in `content.py` under
`SITE.email` and `SOCIALS`) — there is no form or email backend. If a working
contact form is wanted later, wire it to a serverless-friendly service such as
[Resend](https://resend.com) or [Formspree](https://formspree.io).

## Deploy

Deploy anywhere that runs Flask/WSGI — e.g. **Vercel** (Python runtime),
**Render**, **Fly.io**, or **Railway**. Run `npm run build:css` as part of the
build so `static/css/tailwind.css` is current, and serve `app.py` (e.g.
`gunicorn app:app`).

---
© Amit Das
