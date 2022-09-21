import json


def get_text_data(file_data):
    '''
    Принимает json файл, возвращает список
    '''
    with open(file_data, 'r', encoding='utf-8') as file:
        data_list = json.load(file)
    return data_list


def get_posts_by_user(file_data, user_name):
    '''
    Возвращает посты определенного пользователя
    '''
    posts = get_text_data(file_data)
    posts_by_user = []
    is_exists = False
    for post in posts:
        if post['poster_name'] == user_name.lower().strip():
            is_exists = True
            posts_by_user.append(post)
    if not is_exists:
        raise ValueError

    return posts_by_user


def get_comments_by_post_id(file_data, post_id):
    '''
    Возвращает комментарии определенного поста
    '''
    comments = get_text_data(file_data)
    comments_by_post = []
    is_exists = False
    for comment in comments:
        if int(post_id) == comment["post_id"]:
            is_exists = True
            comments_by_post.append(comment)
    if not is_exists:
        raise ValueError

    return comments_by_post


def search_for_posts(posts, query):
    '''
    Возвращает список постов по ключевому слову
    '''
    posts_by_query = []
    i = 1
    for post in posts:
        if i == 10:
            break
        if query.lower().strip() in post["content"].lower().strip():
            i += 1
            posts_by_query.append(post)

    return posts_by_query


def get_post_by_pk(posts, pk):
    '''
    Возвращает один пост по его идентификатору
    '''
    for post in posts:
        if int(pk) == post["pk"]:
            return post
