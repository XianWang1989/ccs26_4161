
import requests

# A predefined mapping of countries to common Accept-Language values
COUNTRY_LANGUAGE_MAP = {
    'US': 'en-US,en;q=0.9',
    'GB': 'en-GB,en;q=0.9',
    'FR': 'fr-FR,fr;q=0.9',
    'DE': 'de-DE,de;q=0.9',
    'RU': 'ru-RU,ru;q=0.9',
    # Add more mappings as needed
}

def get_country_by_ip(ip):
    try:
        response = requests.get(f'https://ipapi.co/{ip}/json/')
        response.raise_for_status()
        data = response.json()
        return data.get('country', 'Unknown')
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def get_default_accept_language(ip):
    country_code = get_country_by_ip(ip)
    if country_code in COUNTRY_LANGUAGE_MAP:
        return COUNTRY_LANGUAGE_MAP[country_code]
    else:
        return 'en-US'  # Default to English if country is unknown

# Example usage
user_ip = '8.8.8.8'  # Replace with the IP address you want to query
accept_language = get_default_accept_language(user_ip)
print(f"Default Accept-Language for {user_ip}: {accept_language}")
