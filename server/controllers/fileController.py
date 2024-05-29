import json

from flask import request, send_from_directory
from flask_login import login_required, current_user

from server import app, PERMITTED_FILE_EXTENSIONS, USER_FILES_DIRECTORY
from server.controllers import role_required
from server.services.user_files import create_file, delete_file


@app.route("/files/create-file", methods=['POST'])
@login_required
def create_file_route():
    try:
        file_bytes = request.files['file'].read()
        filename = request.files['file'].filename
        file_type = request.files['file'].content_type
        user_id = current_user.id

        if len(filename) > 100 or len(filename) < 5 or len(file_bytes) > 6 * (1024 * 1024):
            return json.dumps({
                "message": "length of filename is too big or too small or the size of file is too big (more than 6 mb)"
            })

        if file_type not in PERMITTED_FILE_EXTENSIONS:
            return json.dumps({
                "message": "impossible to upload the file with such extension"
            })

        file_src = create_file(user_id, filename, file_bytes)
        return json.dumps({
            "message": f"file was created",
            "file_src": file_src
        })
    except KeyError:
        return json.dumps({
            "message": "unable to detect a file"
        })


# the route for files directory
@app.route('/files/<path:filename>')
def files(filename):
    return send_from_directory(USER_FILES_DIRECTORY, filename)


@app.route("/files/remove-file", methods=['DELETE'])
@role_required("admin")
def delete_file_route():
    try:
        fileId = int(request.form['fileId'])
        delete_file(fileId)
        return json.dumps({
            "message": "file was deleted"
        })
    except KeyError:
        return json.dumps({
            "message": "file id is not provided"
        })
    except Exception as e:
        return json.dumps({
            "message": f"{e}"
        })
