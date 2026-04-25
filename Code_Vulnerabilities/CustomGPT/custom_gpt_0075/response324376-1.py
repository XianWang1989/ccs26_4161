
import requests

def send_post_request():
    try:
        response = requests.post("https://jsonplaceholder.typicode.com/posts", json={"title": "foo", "body": "bar", "userId": 1})
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

send_post_request()
