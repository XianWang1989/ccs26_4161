
import requests

# Function to get country code from IP
def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    data = response.json()
    return data.get('country', '')

# Mapping of country codes to typical Accept-Language and Accept-Charset
country_language_mapping = {
    "US": {"language": "en-US", "charset": "UTF-8"},
    "RU": {"language": "ru-RU", "charset": "windows-1251"},
    "FR": {"language": "fr-FR", "charset": "UTF-8"},
    "DE": {"language": "de-DE", "charset": "UTF-8"},
    "CN": {"language": "zh-CN", "charset": "UTF-8"},
    # Add more countries as needed
}

# Function to get common headers based on IP
def get_common_headers(ip):
    country_code = get_country_code(ip)
    return country_language_mapping.get(country_code, {"language": "en", "charset": "UTF-8"})

# Example usage
user_ip = '8.8.8.8'  # Example IP
headers = get_common_headers(user_ip)
print(f"Default Accept-Language: {headers['language']}, Accept-Charset: {headers['charset']}")
