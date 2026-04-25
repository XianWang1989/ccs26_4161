
import requests

# Sample mapping of country codes to default language and charset
country_preferences = {
    "US": {"language": "en-US", "charset": "UTF-8"},
    "RU": {"language": "ru-RU", "charset": "windows-1251"},
    "FR": {"language": "fr-FR", "charset": "UTF-8"},
    # Add more countries and their preferences as needed
}

def get_country_from_ip(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    data = response.json()
    return data.get("country")

def get_default_preferences(ip):
    country_code = get_country_from_ip(ip)
    preferences = country_preferences.get(country_code, {"language": "en", "charset": "UTF-8"})
    return preferences

# Example usage
ip_address = '8.8.8.8'  # Replace with the target IP address
default_preferences = get_default_preferences(ip_address)
print(f"Default language: {default_preferences['language']}, charset: {default_preferences['charset']}")
