from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from app import db
from models import Message, User
from .forms import MessageForm

messages = Blueprint('messages', __name__, template_folder='templates')


@messages.route("/new/<username>/", methods=['GET', 'POST'])
@login_required
def send_message(username):
    recipient = username
    user = User.query.filter_by(username=recipient).first_or_404()
    form = MessageForm()
    if form.validate_on_submit():
        msg = Message(author=current_user, recipient=user,
                      body=form.message.data)
        db.session.add(msg)
        db.session.commit()
        flash('Your message has been sent.')
        return redirect(url_for('users.user_messages', username=recipient))
    return render_template('messages/send_message.html', form=form, recipient=recipient, img=user.image_file)


@messages.route("/<int:message_id>")
@login_required
def message(message_id):
    message = Message.query.get_or_404(message_id)
    return render_template('messages/message.html', message=message)


@messages.route("/")
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    messages = Message.query.order_by(Message.timestamp.desc()).paginate(page=page, per_page=5)
    return render_template('messages/_index.html', messages=messages)
