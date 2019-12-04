from flask import Blueprint
from flask import render_template

from models import User
from .forms import UserForm
from flask import request

from app import db
from admin import user_datastore

from flask import redirect
from flask import url_for

from flask_security import login_required

users = Blueprint('users', __name__, template_folder='templates')


@users.route('/create', methods=['POST', 'GET'])
def create_user():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            user = user_datastore.create_user(email=email, password=password, active=True)
            db.session.add(user)
            db.session.commit()

        except:
            print('Something wrong')

        return redirect(url_for('posts.index'))

    form = UserForm()
    return render_template('users/create_user.html', form=form)

#
# @posts.route('/<slug>/edit/', methods=['POST', 'GET'])
# @login_required
# def edit_post(slug):
#     post = Post.query.filter(Post.slug == slug).first_or_404()
#
#     if request.method == 'POST':
#         form = PostForm(formdata=request.form, obj=post)
#         form.populate_obj(post)
#         db.session.commit()
#
#         return redirect(url_for('posts.post_detail', slug=post.slug))
#
#     form = PostForm(obj=post)
#     return render_template('posts/edit_post.html', post=post, form=form)


