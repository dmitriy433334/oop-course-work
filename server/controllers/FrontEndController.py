

from flask import render_template

from server import app


@app.route('/', methods=['GET'])
def index_page():
    return render_template('/front-end/index.html')


@app.route('/login', methods=['GET'])
def login_page():
    return render_template('/front-end/login.html')
