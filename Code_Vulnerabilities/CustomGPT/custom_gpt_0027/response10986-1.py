
import requests

# Sample mapping of country codes to default Accept-Language
country_languages = {
    'US': 'en-US,en;q=0.5',
    'FR': 'fr-FR,fr;q=0.9',
    'DE': 'de-DE,de;q=0.8',
    'RU': 'ru-RU,ru;q=0.9',
    # Add more mappings as needed
}

def get_country_code(ip):
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        data = response.json()
        return data['country']
    except Exception as e:
        print(f"Error fetching country code: {e}")
        return None

def get_accept_language(ip):
    country_code = get_country_code(ip)
    if country_code in country_languages:
        return country_languages[country_code]
    return 'en'  # Default to English if no match found

# Example usage
ip_address = '8.8.8.8'  # Example IP address (change this for real usage)
accept_language = get_accept_language(ip_address)
print(f"Default Accept-Language for {ip_address}: {accept_language}")
