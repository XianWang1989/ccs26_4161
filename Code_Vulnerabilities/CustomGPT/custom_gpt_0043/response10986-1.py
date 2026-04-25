
import requests

# Function to fetch country code based on IP address
def get_country_code(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    if response.status_code == 200:
        return response.json().get('country', 'Unknown')
    else:
        return 'Unknown'

# Function to determine the Accept-Language and Accept-Charset
def determine_language_and_charset(country_code):
    # Dictionary mapping countries to their default languages and charsets
    languages = {
        'US': ('en-US', 'UTF-8'),
        'FR': ('fr-FR', 'UTF-8'),
        'DE': ('de-DE', 'UTF-8'),
        'RU': ('ru-RU', 'windows-1251'),
        'CN': ('zh-CN', 'UTF-8'),
        'JP': ('ja-JP', 'UTF-8'),
        # Add more country codes and their corresponding languages/charsets as needed
    }

    return languages.get(country_code, ('en-US', 'UTF-8'))  # Default to US English if country not found

# Example usage
ip_address = '8.8.8.8'  # Example IP address
country_code = get_country_code(ip_address)  # Get country code
language, charset = determine_language_and_charset(country_code)  # Get language and charset

print(f'Detected language: {language}, charset: {charset}')
