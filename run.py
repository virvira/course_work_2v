import logging
from flask import Flask, jsonify
from main.views import main_blueprint
from utils import get_text_data, get_posts_by_user, get_comments_by_post_id, search_for_posts, get_post_by_pk
import constants

# Создаем экземпляр Flask
app = Flask(__name__)

# Регистрируем блюпринты
app.register_blueprint(main_blueprint)


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.errorhandler(500)
def resource_not_found(e):
    return jsonify(error=str(e)), 500


# Запускаем сервер, только если файл запущен, а не импортирован
if __name__ == "__main__":
    app.run()
