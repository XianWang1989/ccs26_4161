
import requests

def get_country_code(ip):
    """Get the country code from an IP address using an external service."""
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    data = response.json()
    return data.get("country", "")

def get_default_language(country_code):
    """Map country code to the default Accept-Language header."""
    language_map = {
        'US': 'en-US',
        'GB': 'en-GB',
        'DE': 'de-DE',
        'FR': 'fr-FR',
        'RU': 'ru-RU',
        # Add more mappings as needed
    }
    return language_map.get(country_code, 'en-US')  # Default to English

def main(ip):
    country_code = get_country_code(ip)
    if country_code:
        default_language = get_default_language(country_code)
        print(f"Default Accept-Language for {ip}: {default_language}")
    else:
        print("Could not determine country.")

if __name__ == "__main__":
    ip_address = "8.8.8.8"  # Replace with the IP address to check
    main(ip_address)
