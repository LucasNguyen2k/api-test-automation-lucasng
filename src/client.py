import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_post(post_id: int):
    url = f"{BASE_URL}/posts/{post_id}"
    return requests.get(url)
