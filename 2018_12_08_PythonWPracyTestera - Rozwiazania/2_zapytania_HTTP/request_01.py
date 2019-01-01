# WORDPRESS
# https://developer.wordpress.org/rest-api/
# Stworz 2 funkcje umozliwiajace (z pomocą REST API) dodawanie nowych postow oraz
# wypisywanie dat i tytulow postow z wordpressa
#
# add_post_with_json(json)
# printPosts()
#
# http://127.0.0.1/wordpress/wp-json/wp/v2/posts
# login: 'tester'
# password: 'MzB4 Sy7G JejZ c1ag yNJO qSUb' / tester123
# requests.post() - dokumentacja
# request.get() - dokumentacja
# **stworz funkcje umozliwiajaca aktualizowanie istniejacych wpisow

import requests
import json


def get_json_from_file(json_file):
    with open(json_file) as f:
        content = json.load(f)
    return content


def add_post_by_json(json_file):
    content = get_json_from_file(json_file)
    requests.post("http://127.0.0.1/wordpress/wp-json/wp/v2/posts",
                  json=content,
                  auth=('tester', 'MzB4 Sy7G JejZ c1ag yNJO qSUb'))


def print_posts():
    r = requests.get("http://127.0.0.1/wordpress/wp-json/wp/v2/posts")
    for post in r.json():
        print("Date: {}".format(post['date']))
        print("Title: {}".format(post['title']['rendered']))

add_post_by_json("../1_pliki/my_json.json")
print_posts()