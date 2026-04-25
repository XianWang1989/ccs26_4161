
import requests

# Example using requests to make an HTTPS GET request
url = "https://api.github.com/users/octocat"
response = requests.get(url)

if response.status_code == 200:
    user_data = response.json()
    print(f"User: {user_data['login']}")
    print(f"Bio: {user_data['bio']}")
else:
    print("Failed to retrieve data.")
