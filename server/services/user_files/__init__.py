import os

from server import USER_FILES_DIRECTORY, db
from server.database.models.UserFile import UserFile


def get_user_files(user_id):
    return UserFile.query.filter_by(user_id=user_id).all()


def get_userfile(file_id: int) -> UserFile:
    file = UserFile.query.filter_by(id=file_id).first()
    if not file:
        raise Exception(f"file by this id: {file_id} was not found")
    return file


def get_file_src(user_id: int, filename: str):
    return os.path.join(f"{user_id}", f"{filename}")


def create_file(user_id: int, filename: str, file_content: bytes) -> str:
    if not os.path.exists(os.path.join(USER_FILES_DIRECTORY, f"{user_id}")):
        os.mkdir(os.path.join(USER_FILES_DIRECTORY, f"{user_id}"))

    f = open(os.path.join(USER_FILES_DIRECTORY, get_file_src(user_id, filename)), "wb")
    f.write(file_content)
    f.close()

    userFile = UserFile.query.filter_by(file_name=filename, user_id=user_id).first()
    if not userFile:
        userFile = UserFile(file_name=filename, user_id=user_id)

    db.session.add(userFile)
    db.session.commit()

    return get_file_src(user_id, filename)


def delete_file(file_id: int):
    file = UserFile.query.filter_by(id=file_id).first()
    if not file:
        raise Exception(f"file by this id: {file_id} was not found")
    user_id = file.user_id
    filename = file.file_name

    os.remove(os.path.join(USER_FILES_DIRECTORY, f"{user_id}", filename))
    db.session.delete(file)
    db.session.commit()
