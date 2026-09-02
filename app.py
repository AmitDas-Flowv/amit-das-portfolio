"""Flask app for the Amit Das portfolio.

Routes
------
GET  /          → renders the portfolio from ``content.py``.
POST /contact   → validates a contact submission, emails it via SMTP when
                  configured, and always records it to ``contact_submissions.log``
                  as a fallback so the app works out of the box with no secrets.

Email is configured entirely through environment variables (see ``.env.example``);
if ``SMTP_HOST`` is unset the app skips sending and just logs the message.
"""

from __future__ import annotations

import logging
import os
import re
import smtplib
import ssl
from datetime import datetime, timezone
from email.message import EmailMessage
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, abort, jsonify, render_template, request

import content

load_dotenv()

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
SUBMISSIONS_LOG = BASE_DIR / "contact_submissions.log"

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
MAX_LEN = {"name": 120, "email": 200, "message": 4000}

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("portfolio")


@app.route("/")
def index():
    return render_template("index.html", **content.as_context())


@app.route("/work/<slug>")
def work_section(slug):
    """A focused, shareable page for one vertical — e.g. /work/fashion."""
    group = content.group_for(slug)
    if group is None:
        abort(404)
    return render_template("section.html", group=group, **content.as_context())


@app.route("/contact", methods=["POST"])
def contact():
    # Honeypot — a real user never fills the hidden "company" field.
    if (request.form.get("company") or "").strip():
        # Pretend success so bots get no signal.
        return jsonify(ok=True, message="Thank you — your message is on its way.")

    name = (request.form.get("name") or "").strip()
    email = (request.form.get("email") or "").strip()
    message = (request.form.get("message") or "").strip()

    error = _validate(name, email, message)
    if error:
        return jsonify(ok=False, error=error), 400

    record = {
        "at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "name": name,
        "email": email,
        "message": message,
        "ip": request.headers.get("X-Forwarded-For", request.remote_addr),
    }
    _log_submission(record)

    try:
        _maybe_send_email(record)
    except Exception:  # noqa: BLE001 — never leak SMTP errors to the client
        logger.exception("Contact email delivery failed")
        # The submission is safely logged, so still report success to the user.

    return jsonify(ok=True, message="Thank you — your message is on its way.")


def _validate(name: str, email: str, message: str) -> str | None:
    if not name or not email or not message:
        return "Please fill in your name, email and message."
    if len(name) > MAX_LEN["name"] or len(email) > MAX_LEN["email"] or len(
        message
    ) > MAX_LEN["message"]:
        return "One of the fields is too long."
    if not EMAIL_RE.match(email):
        return "That email address doesn’t look right."
    return None


def _log_submission(record: dict) -> None:
    line = (
        f"[{record['at']}] {record['name']} <{record['email']}> "
        f"({record['ip']}): {record['message']}\n"
    )
    try:
        with SUBMISSIONS_LOG.open("a", encoding="utf-8") as fh:
            fh.write(line)
    except OSError:
        logger.exception("Could not write to %s", SUBMISSIONS_LOG)


def _maybe_send_email(record: dict) -> None:
    host = os.getenv("SMTP_HOST")
    if not host:
        logger.info("SMTP not configured — submission logged only.")
        return

    port = int(os.getenv("SMTP_PORT", "587"))
    user = os.getenv("SMTP_USER")
    password = os.getenv("SMTP_PASS")
    recipient = os.getenv("CONTACT_TO") or content.SITE["email"]
    sender = os.getenv("MAIL_FROM") or user or recipient

    msg = EmailMessage()
    msg["Subject"] = f"Portfolio enquiry from {record['name']}"
    msg["From"] = sender
    msg["To"] = recipient
    msg["Reply-To"] = record["email"]
    msg.set_content(
        f"Name: {record['name']}\n"
        f"Email: {record['email']}\n"
        f"IP: {record['ip']}\n"
        f"Time: {record['at']}\n\n"
        f"{record['message']}\n"
    )

    context = ssl.create_default_context()
    with smtplib.SMTP(host, port, timeout=15) as server:
        server.starttls(context=context)
        if user and password:
            server.login(user, password)
        server.send_message(msg)
    logger.info("Contact email sent to %s", recipient)


if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=debug)
