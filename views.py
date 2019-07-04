from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import  ContactForm, CareerForm
from werkzeug import secure_filename

import smtplib
import os
from email.message import EmailMessage

main = Blueprint('main', __name__)

@main.route('/test')
def test():
    return render_template('test.html')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/careers', methods=['GET', 'POST'])
def careers():
    form = CareerForm()
    name = form.name.data
    email = form.email.data
    cover = form.cover.data
    F = [form.file_r, form.file_c]
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('careers.html', form=form)
        else:
            msg = EmailMessage()
            msg['Subject'] = 'Resume Request' 
            msg['From'] = 'hello@blankstudio.ca'
            msg['To'] = 'hello@blankstudio.ca'
            msg.set_content("""
            Email: {}
            Name: {}

            Cover Letter:
            
            {}
            """.format(email, name, cover))
            for f in F:
                if f.data is not None:
                    file_data = f.data.read()
                    file_name = f.data.filename
                    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

            with smtplib.SMTP_SSL('smtp.yandex.com', 465) as smtp:
                smtp.login('hello@blankstudio.ca', 'kmani123')
                smtp.send_message(msg)
            return render_template('careers.html', success=True)

    else:
        return render_template('careers.html', form=form)

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/project', methods=['GET', 'POST'])
def project():
    form = ContactForm()
    name = form.name.data
    email = form.email.data
    message = form.message.data
    project_type = form.subject.data
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('project.html', form=form)
        else:
            msg = EmailMessage()
            msg['Subject'] = 'Project Request' 
            msg['From'] = 'hello@blankstudio.ca'
            msg['To'] = 'hello@blankstudio.ca'
            msg.set_content("""
            Email: {}
            Name: {}
            Project Type: {}

            Message:
            
            {}
            """.format(email, project_type, name, message))

            with smtplib.SMTP_SSL('smtp.yandex.com', 465) as smtp:
                smtp.login('hello@blankstudio.ca', 'kmani123')
                smtp.send_message(msg)
            return render_template('project.html', success=True)
 
    elif request.method == 'GET':
        return render_template('project.html', form=form)

@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404