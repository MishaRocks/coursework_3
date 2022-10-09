import os

from flask import Flask, render_template

from app.bookmarks.bm_views import bookmarks_blueprint
from app.posts.posts_views import posts_blueprint
from app.api.utils import api_blueprint

# POST_PATH = os.path.dirname(os.path.abspath('app', 'data', 'posts.json'))
# UPLOAD_FOLDER = "uploads/images"


# CONFIG_PATH = os.path.join(ROOT_DIR, 'data/posts.json')


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False



# Регистрирую блюпринты
app.register_blueprint(posts_blueprint)
app.register_blueprint(api_blueprint)
app.register_blueprint(bookmarks_blueprint)


# Считываем ошибки
@app.errorhandler(404)
def handle_bad_request(error):
    return render_template('404.html')


@app.errorhandler(500)
def handle_bad_request(error):
    return render_template('500.html')


if __name__ == "__main__":
    app.run()
