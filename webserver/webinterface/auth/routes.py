from datetime import timedelta, datetime
from functools import wraps

from flask import render_template, flash, redirect, session, request, url_for
from flask_login import current_user, login_user, logout_user
from sqlalchemy import select

from webserver.database.models.posting import Posting
from webserver.database.models.user import User
from webserver.webinterface.auth import auth_bp
from webserver.webinterface.auth.forms import LoginForm, RegistrationForm
from webserver.webinterface.persistancelayer import PersistenceLayer


@auth_bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    with PersistenceLayer.db().get_db_session() as db_session:
        my_posts = (
            db_session.query(Posting)
            .join(Posting.author)  # Join über die Beziehung 'author'
            .filter(User.username == current_user.username)
            .order_by(Posting.created_on.desc())
            .limit(3)
            .all()
        )

        other_posts = (
            db_session.query(Posting)
            .join(Posting.author)  # Join über die Beziehung 'author'
            .filter(User.username != current_user.username)
            .order_by(Posting.created_on.desc())
            .limit(3)
            .all()
        )
        my_posts_ser = [post.to_dict() for post in my_posts]
        other_posts_ser = [post.to_dict() for post in other_posts]
    return render_template('dashboard.html', title='Dashboard', my_posts_ser=my_posts_ser, other_posts_ser=other_posts_ser)


@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        with PersistenceLayer.db().get_db_session() as db_session:
            user = db_session.scalar(
                select(User).where(User.username == form.username.data))
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password', category='error')
                return redirect(url_for('auth.login'))
            user.last_login = datetime.now()
            login_user(user)
            return redirect(url_for('auth.dashboard'))
    return render_template('auth/login.html', title='Sign In', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))



@auth_bp.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)

        with PersistenceLayer.db().get_db_session() as db_session:
            db_session.add(user)
            db_session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Register', form=form)