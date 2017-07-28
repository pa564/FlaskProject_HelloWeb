from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import NameForm
from .. import db
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
        form_app = NameForm()
        if form_app.validate_on_submit():
		user_app = User.query.filter_by(username=form_app.name_index_input.data).first()
		if user_app is None:
			user_app = User(username=form_app.name_index_input.data)
			db.session.add(user_app)
			session['known'] = False
			if app.config['FLASK_ADMIN']:
				send_email(app.config['FLASK_ADMIN'], '新用户', 'mail/new_user', user=user_app)
		else:
			session['known'] = True

		session['name'] = form_app.name_index_input.data
		form_app.name_index_input.data = ''

                return redirect(url_for('.index'))

        return render_template('index.html', form_index=form_app, name_index_display=session.get('name'), known=session.get('known', False), current_time=datetime.utcnow())

