from flask import Flask
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
# from flask_frozen import Freezer
import git
import os
import hmac
import hashlib

# def create_app():
app = Flask(__name__)
# app.config.from_pyfile('settings.py')
app.secret_key = 'development key'


# freezer = Freezer(app)

def is_valid_signature(x_hub_signature, data, private_key):
    # x_hub_signature and data are from the webhook payload
    # private key is your webhook secret
    hash_algorithm, github_signature = x_hub_signature.split('=', 1)
    algorithm = hashlib.__dict__.get(hash_algorithm)
    encoded_key = bytes(private_key, 'latin-1')
    mac = hmac.new(encoded_key, msg=data, digestmod=algorithm)
    return hmac.compare_digest(mac.hexdigest(), github_signature)

w_secret = os.getenv('WEBHOOK_SECRET')

@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        abort_code = 418
        x_hub_signature = request.headers.get('X-Hub-Signature')
        # webhook content type should be application/json for request.data to have the payload
        # request.data is empty in case of x-www-form-urlencoded
        if not is_valid_signature(x_hub_signature, request.data, w_secret):
            print('Deploy signature failed: {sig}'.format(sig=x_hub_signature))
            abort(abort_code)
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


    # return(app)
