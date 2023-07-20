from flask import render_template

from app.recordings import bp


@bp.route("/")
def index():
    return render_template("recordings/index.html")
