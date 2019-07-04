from flask import Flask
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template, request, redirect, url_for, flash

def create_app():
    app = Flask(__name__)
    app.secret_key = 'development key'


    from .views import main
    app.register_blueprint(main)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404


    return(app)
