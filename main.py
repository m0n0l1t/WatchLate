from admin import *
from posts.blueprint_post import posts
from users.blueprint_user import users

import view

app.register_blueprint(posts, url_prefix='/blog')
app.register_blueprint(users, url_prefix='/profile')


if __name__ == '__main__':
    app.run()
