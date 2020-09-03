# from admin import *
from app import app
from posts.blueprint_post import posts
from users.blueprint_user import users
from main.blueprint_main import main
from messages.blueprint_messages import messages
from models import db

import view

db.create_all()
app.register_blueprint(posts, url_prefix='/posts')
app.register_blueprint(users)
app.register_blueprint(main)
app.register_blueprint(messages, url_prefix='/messages')


if __name__ == '__main__':
    app.run()


