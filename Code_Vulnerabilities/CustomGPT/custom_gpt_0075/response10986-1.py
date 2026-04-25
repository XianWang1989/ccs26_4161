
import requests

# Static mappings for demonstration
country_language_mapping = {
    'US': ('en-US', 'utf-8'),
    'FR': ('fr-FR', 'utf-8'),
    'DE': ('de-DE', 'utf-8'),
    # Add more mappings as needed
}

def get_country_code(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        data = response.json()
        return data['countryCode'] if data['status'] == 'success' else None
    except Exception as e:
        print(f"Error: {e}")
        return None

def determine_language_and_charset(ip):
    country_code = get_country_code(ip)
    if country_code in country_language_mapping:
        return country_language_mapping[country_code]
    return ('en', 'utf-8')  # Default fall-back

# Example use
ip_address = '8.8.8.8'  # Example IP
language, charset = determine_language_and_charset(ip_address)
print(f"Language: {language}, Charset: {charset}")
