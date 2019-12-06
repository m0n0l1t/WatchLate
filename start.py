from admin import *
from posts.blueprint_post import posts
from users.blueprint_user import users
from main.blueprint_main import main

import view

app.register_blueprint(posts, url_prefix='/blog')
app.register_blueprint(users, url_prefix='/profile')
app.register_blueprint(main, url_prefix='/main')


if __name__ == '__main__':
    app.run()
