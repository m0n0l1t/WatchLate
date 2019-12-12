from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from app import db
from models import Post
from.forms import PostForm

posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route("/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()

    if form.validate_on_submit():
        link = form.youtube_link.data.split('/')
        youtube = link[len(link) - 1]
        url = '''https://www.youtube.com/embed/''' + youtube
        post = Post(title=form.title.data,
                    content=form.content.data,
                    youtube_link=url,
                    author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('posts/create_post.html', title='New Post',
                           form=form, legend='New Post')


@posts.route("/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('posts/post.html', title=post.title, post=post)


@posts.route("/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)

    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():

        link = form.youtube_link.data.split('/')
        youtube = link[len(link) - 1]
        url = '''https://www.youtube.com/embed/''' + youtube
        post.title = form.title.data
        post.content = form.content.data
        post.youtube_link = url
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.youtube_link.data = post.youtube_link
    return render_template('posts/create_post.html', title='Update Post',
                           form=form, legend='Update Post')

@posts.route('/')
def index():
    q = request.args.get('q')

    page = request.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q))  # .all()
    else:
        posts = Post.query.order_by(Post.created.desc())

    pages = posts.paginate(page=page, per_page=5)

    return render_template('posts/index.html', pages=pages)


@posts.route("/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))
