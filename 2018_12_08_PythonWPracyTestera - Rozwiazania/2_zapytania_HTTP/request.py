import requests

r = requests.get("http://192.168.100.197/wordpress/wp-json/wp/v2/posts")
print(r.status_code)
print(r.headers)
print(r.json())
