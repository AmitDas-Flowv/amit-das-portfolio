# Amit Das — Portfolio

Personal portfolio site for **Amit Das** — AI Director & Creative Director
(luxury, jewellery & fashion), grounded in thirteen years of filmmaking,
cinematography and post.

Built as a small **Flask** app with the frontend styled in **Tailwind CSS**.
All page content lives in `content.py`, rendered through Jinja2 templates, and
the contact section posts to a working backend endpoint.

## Stack & layout

```
app.py                 Flask app — GET / and POST /contact
content.py             All page copy as Python data
templates/
  base.html            <head>, nav, atmosphere layers, footer, scripts
  index.html           Sections, rendered from content.py + contact form
src/input.css          Tailwind entry + custom cinema-effect layer
tailwind.config.js     Design tokens (palette, fonts, type scale, animations)
static/css/tailwind.css  Built stylesheet (generated; committed so it runs w/o Node)
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

Open <http://localhost:5000>.

While editing styles, run `npm run watch:css` in a second terminal to rebuild
`static/css/tailwind.css` automatically.

## Contact form

`POST /contact` validates the submission (required fields, email format, plus a
hidden honeypot field that traps bots) and then:

- **With SMTP configured** — emails the message to `CONTACT_TO`.
- **Without SMTP** — appends it to `contact_submissions.log` and still reports
  success, so the app runs out of the box with no configuration.

To enable email, copy `.env.example` to `.env` and fill in the `SMTP_*` and
`CONTACT_TO` values (for Gmail, use an [App Password](https://support.google.com/accounts/answer/185833)).

## Deploy

This is now a Python web app (not a purely static site), so the contact
endpoint needs a running server. Deploy anywhere that runs Flask/WSGI —
e.g. **Render**, **Fly.io**, **Railway**, or **Vercel** (Python runtime).
Run `npm run build:css` as part of the build so `static/css/tailwind.css` is
up to date, set the `SMTP_*` environment variables for email, and serve
`app.py` with a production WSGI server such as `gunicorn app:app`.

---
© Amit Das
