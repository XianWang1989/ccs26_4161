
import requests
from flask import Flask, request

app = Flask(__name__)

# A mapping of country codes to common language and charset preferences
country_preferences = {
    'US': {'language': 'en-US', 'charset': 'UTF-8'},
    'RU': {'language': 'ru-RU', 'charset': 'windows-1251'},
    'FR': {'language': 'fr-FR', 'charset': 'UTF-8'},
    # Add more country preferences as needed
}

def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/country/')
    return response.text if response.status_code == 200 else None

@app.route('/')
def index():
    user_ip = request.remote_addr
    country_code = get_country_code(user_ip)

    if country_code in country_preferences:
        preferences = country_preferences[country_code]
        return f"Common Language: {preferences['language']}, Common Charset: {preferences['charset']}"
    return "No preferences found for your location."

if __name__ == '__main__':
    app.run()
