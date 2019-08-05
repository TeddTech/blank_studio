from flask import Flask
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template, request, redirect, url_for, flash
# from flask_frozen import Freezer
import git

# def create_app():
app = Flask(__name__)
# app.config.from_pyfile('settings.py')
app.secret_key = 'development key'


# freezer = Freezer(app)

@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('blank/blank_studio')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400



from .views import main
app.register_blueprint(main)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


    # return(app)shz zz
