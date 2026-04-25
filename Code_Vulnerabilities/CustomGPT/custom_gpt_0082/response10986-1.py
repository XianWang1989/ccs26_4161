
import requests

# Function to get country code from IP address
def get_country_code(ip_address):
    response = requests.get(f"https://ipapi.co/{ip_address}/country/")
    return response.text if response.status_code == 200 else None

# Function to map country code to default Accept-Language and Accept-Charset
def get_default_accept_headers(country_code):
    language_map = {
        'US': ('en-US', 'utf-8'),
        'FR': ('fr-FR', 'utf-8'),
        'DE': ('de-DE', 'utf-8'),
        'RU': ('ru-RU', 'windows-1251'),
        # Add more country mappings as needed
    }

    return language_map.get(country_code, ('en', 'utf-8'))  # Default to English

# Example usage
if __name__ == "__main__":
    ip_address = '134.201.250.155'  # Example IP
    country_code = get_country_code(ip_address)

    if country_code:
        language, charset = get_default_accept_headers(country_code)
        print(f"Default Accept-Language: {language}, Accept-Charset: {charset}")
    else:
        print("Could not determine the country code.")
