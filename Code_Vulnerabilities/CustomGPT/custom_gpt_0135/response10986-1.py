
import requests

# Sample mapping of country codes to default Accept-Language and Accept-Charset
country_preferences = {
    'US': {
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Charset': 'UTF-8, ISO-8859-1;q=0.9'
    },
    'RU': {
        'Accept-Language': 'ru-RU,ru;q=0.9',
        'Accept-Charset': 'windows-1251,UTF-8;q=0.9'
    },
    'CN': {
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Charset': 'UTF-8'
    },
    # Add more country preferences as needed
}

def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    data = response.json()
    return data.get('country', None)

def get_default_headers(ip):
    country_code = get_country_code(ip)
    if country_code and country_code in country_preferences:
        return country_preferences[country_code]
    return None

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP address
default_headers = get_default_headers(ip_address)

if default_headers:
    print("Default headers based on IP:")
    print(default_headers)
else:
    print("Country code not found or no preferences available.")
