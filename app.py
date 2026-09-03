"""Flask app for the Amit Das portfolio.

Routes
------
GET /              → renders the portfolio from ``content.py``.
GET /work/<slug>   → a focused, shareable page for one work vertical.

Contact is a plain ``mailto:`` link — there is no form endpoint.
"""

from __future__ import annotations

import os

from flask import Flask, abort, render_template

import content

app = Flask(__name__)


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


if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=debug)
