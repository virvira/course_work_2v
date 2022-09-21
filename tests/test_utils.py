import pytest
import constants

from utils import get_text_data, get_posts_by_user, get_comments_by_post_id, search_for_posts, get_post_by_pk


def test_get_text_data_attribute_error():
    with pytest.raises(AttributeError):
        data_list = get_text_data(constants.POSTS_ILE)


def test_get_text_data_file_not_found():
    with pytest.raises(FileNotFoundError):
        data_list = get_text_data('privet')


def test_get_text_data_type_error():
    with pytest.raises(TypeError):
        data_list = get_text_data()


def test_get_text_data_file_open():
    data_list = get_text_data(constants.POSTS_FILE)
    assert type(data_list) == list, "Ошибка преобразования в список"


def test_get_posts_by_user_null():
    with pytest.raises(ValueError):
        posts_by_user = get_posts_by_user(constants.POSTS_FILE, 'user2019')


def test_get_posts_by_user_type_error():
    with pytest.raises(TypeError):
        data_list = get_posts_by_user(constants.POSTS_FILE)


def test_get_posts_by_user_leo():
    posts_by_user = get_posts_by_user(constants.POSTS_FILE, 'leo')
    assert posts_by_user is not []


def test_get_comments_by_post_id_null():
    with pytest.raises(ValueError):
        comments_by_user = get_comments_by_post_id(constants.COMMENTS_FILE, 101010)


def test_get_comments_by_post_id_one():
    comments_by_user = get_comments_by_post_id(constants.COMMENTS_FILE, 1)
    assert comments_by_user is not []


def test_get_comments_by_post_id_type_error():
    with pytest.raises(TypeError):
        data_list = get_comments_by_post_id(constants.COMMENTS_FILE)


def test_search_for_posts_null():
    posts = get_text_data(constants.POSTS_FILE)
    posts_by_query = search_for_posts(posts, "одномоментный")
    assert posts_by_query == []


def test_search_for_posts_walk():
    posts = get_text_data(constants.POSTS_FILE)
    posts_by_query = search_for_posts(posts, "погулять")
    assert posts_by_query is not []


def test_search_for_posts_walk_type_error():
    with pytest.raises(TypeError):
        posts = get_text_data(constants.POSTS_FILE)
        posts_by_query = search_for_posts(posts)


def test_get_post_by_pk_none():
    posts = get_text_data(constants.POSTS_FILE)
    post = get_post_by_pk(posts, 1109)
    assert post is None


def test_get_post_by_pk_one():
    posts = get_text_data(constants.POSTS_FILE)
    post = get_post_by_pk(posts, 1)
    assert post is not None


def test_get_post_by_pk_type_error():
    with pytest.raises(TypeError):
        posts = get_text_data(constants.POSTS_FILE)
        post = get_post_by_pk(posts)
