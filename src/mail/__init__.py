import threading

from flask import current_app, render_template
from flask_mail import Message, Mail

mail = Mail()


def send_mail(to, subject, template, **kwargs):
    msg = Message(current_app.config["FLASK_MAIL_SUBJECT_PREFIX"] + subject,
                  sender=current_app.config['FLASK_MAIL_SENDER'],
                  recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    app = current_app._get_current_object()
    th_send_mail = threading.Thread(target=async_send_mail, args=(app, msg))
    th_send_mail.start()
    return th_send_mail


def async_send_mail(app, msg):
    with app.app_context():
        mail.send(msg)
