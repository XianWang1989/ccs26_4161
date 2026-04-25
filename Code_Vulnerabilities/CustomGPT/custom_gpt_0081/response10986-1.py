
from flask import Flask, request
import requests

app = Flask(__name__)

# Sample mapping of country codes to default language and charset
country_language_mapping = {
    'US': ('en-US', 'UTF-8'),
    'GB': ('en-GB', 'UTF-8'),
    'RU': ('ru-RU', 'windows-1251'),
    'FR': ('fr-FR', 'ISO-8859-1'),
    # Add more country codes and their corresponding locales
}

def get_country_code(ip):
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    data = response.json()
    return data.get('country')

@app.route('/')
def index():
    # Get the user's IP address
    user_ip = request.remote_addr
    country_code = get_country_code(user_ip)

    if country_code in country_language_mapping:
        language, charset = country_language_mapping[country_code]
    else:
        language, charset = ('en-US', 'UTF-8')  # Default values if country not found

    return f'Detected Language: {language}, Charset: {charset}'

if __name__ == '__main__':
    app.run(debug=True)
