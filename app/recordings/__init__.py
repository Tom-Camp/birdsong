from flask import Blueprint

bp = Blueprint("recordings", __name__)

from app.recordings import routes  # noqa: E402 F401
