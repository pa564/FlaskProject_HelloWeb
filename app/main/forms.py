from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask import session, redirect, url_for, flash


class NameForm(Form):
        name_index_input = StringField('填写你的ID: ', validators=[Required()])
        submit_index = SubmitField('提交')
