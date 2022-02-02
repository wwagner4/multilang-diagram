from pathlib import Path

import flask
from flask import Flask

app = Flask(__name__)

base_dir = Path(__file__).parent.parent
dist_dir = base_dir / "vuegui" / "dist"


@app.route("/<path1>/<path2>/<file>")
def paths(path1: str, path2: str, file: str):
    return file_response(dist_dir / path1 / path2 / file)


@app.route("/<path>/<file>")
def one_path(path: str, file: str):
    return file_response(dist_dir / path / file)


@app.route("/<file>")
def no_path(file: str):
    return file_response(dist_dir / file)


@app.route("/")
def base():
    return file_response(dist_dir / "index.html")


def file_response(file: Path) -> flask.Response:
    file_name = str(file)
    if file_name.endswith("html"):
        return flask.send_file(file, mimetype='text/html')
    if file_name.endswith("png"):
        return flask.send_file(file, mimetype='image/png')
    if file_name.endswith("ico"):
        return flask.send_file(file, mimetype='image/x-icon')
    if file_name.endswith("js"):
        return flask.send_file(file, mimetype='application/javascript')
    if file_name.endswith("css"):
        return flask.send_file(file, mimetype='text/css')
    return flask.send_file(file, mimetype='application/octet-stream')
