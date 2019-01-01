import requests

r = requests.get("http://127.0.0.1/wordpress/wp-json/wp/v2/posts")
print(r.status_code)
print(r.headers)
print(r.json())
