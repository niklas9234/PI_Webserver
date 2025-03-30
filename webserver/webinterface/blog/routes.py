from flask import render_template, url_for
from flask_login import current_user, login_required
from werkzeug.utils import redirect

from webserver.database.models.posting import Posting
from webserver.database.models.user import User
from webserver.webinterface.blog import blog_bp
from webserver.webinterface.blog.forms import CreatePostForm
from webserver.webinterface.persistancelayer import PersistenceLayer


@blog_bp.route('/my_posts', methods=['GET', 'POST'])
@login_required
def my_posts():
    with PersistenceLayer.db().get_db_session() as db_session:
        my_posts = (
            db_session.query(Posting)
            .join(Posting.author)
            .filter(User.username == current_user.username)
            .order_by(Posting.created_on.desc())
            .all()
        )
        posts_ser = [post.to_dict() for post in my_posts]
    return render_template('blog/my_posts.html', title='My Posts', posts=posts_ser)


@blog_bp.route('/explore', methods=['GET', 'POST'])
@login_required
def explore():
    with PersistenceLayer.db().get_db_session() as db_session:
        posts = (
            db_session.query(Posting)
            .join(Posting.author)
            .order_by(Posting.created_on.desc())
            .all()
        )
        posts_ser = [post.to_dict() for post in posts]
    return render_template('blog/explore.html', title='Explore', posts=posts_ser )

@blog_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = Posting(
            title=form.title.data,
            body=form.content.data,
            user_id=current_user.id
        )
        with PersistenceLayer.db().get_db_session() as db_session:
            db_session.add(new_post)
            db_session.commit()
        return redirect(url_for('auth.dashboard'))

    return render_template('blog/create.html', title='Create', form=form )