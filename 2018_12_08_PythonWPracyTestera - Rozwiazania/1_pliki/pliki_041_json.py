
# Stworz funkcje tworzaca plik json zawierajacy
# {'date': '2018-06-30T20:00:35',
# 'title': 'Imię - moj post',
# 'status': 'publish',
# 'content': 'content',
# 'excerpt': 'Exceptional post!',
# 'format': 'standard'
# }

import json

def create_json():
    post = {'date': '2018-06-29T20:00:35',
            'title': 'Jakub - moj post',
            'status': 'publish',
            'content': 'content',
            'excerpt': 'Exceptional post!',
            'format': 'standard'
            }

    with open("post.json", 'w') as f:
        json.dump(post, f)

create_json()
