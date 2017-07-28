from . import app, mail


def send_async_email(app, msg):
        with app.app_context():
                mail.send(msg)

def send_email(to, subject,template, user):
        msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
        msg.body = 'test'
        msg.html = 'test'
        thr = Thread(target=send_async_email, args=[app, msg])
        thr.start()
        return thr
