from flask_wtf import FlaskForm
from sqlalchemy import select

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired

from webserver.database.models.user import User
from webserver.webinterface.persistancelayer import PersistenceLayer


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        with PersistenceLayer.db().get_db_session() as db_session:
            user = db_session.scalar(select(User).where(
            User.username == username.data))
            if user is not None:
                raise ValidationError('Please use a different username!')

