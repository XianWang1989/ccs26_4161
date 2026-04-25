
from flask import Flask, request, jsonify

app = Flask(__name__)

# Example mapping: country code -> (Accept-Language, Accept-Charset)
country_preferences = {
    'US': ('en-US,en;q=0.9', 'utf-8'),
    'RU': ('ru-RU,ru;q=0.9', 'windows-1251'),
    'FR': ('fr-FR,fr;q=0.9', 'utf-8'),
    # Add more countries and their preferences as needed
}

def get_country_code(ip):
    # Implementation to get country code from IP (use an external API or service)
    # For demonstration, let's return 'US' for any IP (replace this with real lookup)
    return 'US'

@app.route('/')
def index():
    user_ip = request.remote_addr  # Get user's IP address
    country_code = get_country_code(user_ip)

    if country_code in country_preferences:
        accept_language, accept_charset = country_preferences[country_code]
    else:
        accept_language, accept_charset = ('en-US,en;q=0.9', 'utf-8')  # Default values

    response = jsonify(message="Hello, world!")
    response.headers['Accept-Language'] = accept_language
    response.headers['Accept-Charset'] = accept_charset

    return response

if __name__ == '__main__':
    app.run(debug=True)
