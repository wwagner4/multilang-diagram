from pathlib import Path

import flask
import os
import multilangdia.createdia as cd

app = flask.Flask(__name__)

web_public_name = 'VUE_DISTRIBUTION_DIR'
out_dir_path = os.getenv(web_public_name)
if not out_dir_path:
    raise AttributeError(f"Environment variable {web_public_name} must be defined")
dist_dir = Path(out_dir_path)
if not dist_dir.exists():
    raise AttributeError(f"Output directory {dist_dir} must exist")


@app.route("/<path1>/<path2>/<file>")
def paths(path1: str, path2: str, file: str):
    return file_response(dist_dir / path1 / path2 / file)


@app.route("/<path>/<file>")
def one_path(path: str, file: str):
    return file_response(dist_dir / path / file)


@app.route("/<file>")
def no_path(file: str):
    return file_response(dist_dir / file)


@app.route("/create", methods=["POST"])
def create():
    data = flask.request.get_json()
    print(f"received {data}")
    file_name = cd.create_diagram(dist_dir, data["x_label"], data["y_label"], data["z_label"])
    print(f"created {file_name} in {dist_dir.absolute()}")
    return file_name


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
