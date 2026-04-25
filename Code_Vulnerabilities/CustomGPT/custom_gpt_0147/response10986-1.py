
from flask import Flask, request
import requests

app = Flask(__name__)

# Replace with a real geolocation service URL
GEOLOCATION_API_URL = 'https://api.ipgeolocation.io/ipgeo?apiKey=YOUR_API_KEY&ip={}'

language_map = {
    "US": "en-US",
    "DE": "de-DE",
    "FR": "fr-FR",
    "RU": "ru-RU",
}

charset_map = {
    "US": "UTF-8",
    "DE": "ISO-8859-1",
    "FR": "ISO-8859-1",
    "RU": "windows-1251",
}

def get_country_code_from_ip(ip):
    response = requests.get(GEOLOCATION_API_URL.format(ip)).json()
    return response.get('country_code2', 'US')  # Default to US if not found

def get_default_language(country_code):
    return language_map.get(country_code, "en-US")

def get_default_charset(country_code):
    return charset_map.get(country_code, "UTF-8")

@app.route('/')
def index():
    user_ip = request.remote_addr  # Get user IP
    country_code = get_country_code_from_ip(user_ip)
    language = get_default_language(country_code)
    charset = get_default_charset(country_code)

    return f"Detected Language: {language}, Charset: {charset}"

if __name__ == "__main__":
    app.run(debug=True)
