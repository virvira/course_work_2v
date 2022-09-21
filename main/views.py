import logging

from flask import Blueprint, jsonify
from flask import Flask, request, render_template

from logger import api_logger
from utils import get_text_data, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user
import constants

# Cоздаем новый блюпринт, выбираем для него имя
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


# Создаем вьюшки
@main_blueprint.route('/')
def page_index():
    posts = get_text_data(constants.POSTS_FILE)
    return render_template('index.html', posts=posts)


@main_blueprint.route('/posts/<postid>')
def one_post(postid):
    posts = get_text_data(constants.POSTS_FILE)
    post = get_post_by_pk(posts, postid)
    comments = get_comments_by_post_id(constants.COMMENTS_FILE, postid)
    comments_count = len(comments)
    return render_template('post.html', post=post, comments=comments, comments_count=comments_count)


@main_blueprint.route('/search')
def search_result():
    posts = get_text_data(constants.POSTS_FILE)
    s = request.args.get('s', '')
    if s is None:
        return 'Введите параметр для поиска'
    # logging.info("Страница с результатами поиска")
    res = search_for_posts(posts, s)
    posts_count = len(res)
    return render_template('search.html', res=res, s=s, posts_count=posts_count)


@main_blueprint.route('/users/<username>')
def user_posts(username):
    posts_by_user = get_posts_by_user(constants.POSTS_FILE, username)
    return render_template('user-feed.html', posts_by_user=posts_by_user)


@main_blueprint.route('/api/posts', methods=["GET"])
def read_posts():
    api_logger.info("Запрос к /api/posts")
    posts = get_text_data(constants.POSTS_FILE)
    return jsonify(posts)


@main_blueprint.route('/api/posts/<post_id>', methods=["GET"])
def read_post(post_id):
    api_logger.info("Запрос /api/posts/<post_id>")
    posts = get_text_data(constants.POSTS_FILE)
    post = get_post_by_pk(posts, post_id)
    return jsonify(post)
