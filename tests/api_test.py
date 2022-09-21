import pytest
import json

from run import app

post_keys = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}


def test_read_posts():
    response = app.test_client().get('/api/posts')
    data = response.json
    keys = set((response.json[0]).keys())

    assert response.status_code == 200
    assert type(data) == list
    assert keys == post_keys


def test_read_one_post():
    response = app.test_client().get('/api/posts/1')
    data = response.json
    keys = set(response.json.keys())

    assert response.status_code == 200
    assert type(data) == dict
    assert keys == post_keys
