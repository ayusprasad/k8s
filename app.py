from __future__ import annotations

import os

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if not name:
            message = "Please enter your name."
        elif len(name) > 80:
            message = "Name must be 80 characters or fewer."
        else:
            message = f"Hello {name}, welcome to the Kubernetes test application."
    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", "5000")),
        debug=False,
    )
