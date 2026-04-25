
import requests

# Example mapping of country codes to popular Accept-Language and Accept-Charset
country_preferences = {
    'US': {'language': 'en-US', 'charset': 'UTF-8'},
    'RU': {'language': 'ru-RU', 'charset': 'windows-1251'},
    'FR': {'language': 'fr-FR', 'charset': 'UTF-8'},
    # Add more country mappings as needed
}

def get_country_by_ip(ip):
    try:
        response = requests.get(f'https://ipapi.co/{ip}/json/')
        data = response.json()
        return data.get('country')
    except Exception as e:
        print(f"Error retrieving country: {e}")
        return None

def get_default_preferences(ip):
    country_code = get_country_by_ip(ip)
    if country_code and country_code in country_preferences:
        return country_preferences[country_code]
    return None

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP address
preferences = get_default_preferences(ip_address)

if preferences:
    print(f"Default Accept-Language: {preferences['language']}")
    print(f"Default Accept-Charset: {preferences['charset']}")
else:
    print("Country not found or preferences not defined.")
