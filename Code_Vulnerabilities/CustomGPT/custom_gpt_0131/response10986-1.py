
import requests

# Example function to get country code from IP address
def get_country_code(ip_address):
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    data = response.json()
    return data.get('country')

# Function to get default Accept-Language based on country code
def get_default_accept_language(country_code):
    # Define mapping of country code to popular Accept-Language headers
    language_map = {
        'US': 'en-US',
        'GB': 'en-GB',
        'FR': 'fr-FR',
        'DE': 'de-DE',
        'RU': 'ru-RU',
        'CN': 'zh-CN',
        # Add more mappings as necessary
    }
    return language_map.get(country_code, 'en')  # Default to 'en' if country not found

# Example usage
ip_address = '8.8.8.8'  # Replace with the user's IP address
country_code = get_country_code(ip_address)
accept_language = get_default_accept_language(country_code)

print(f"IP Address: {ip_address}")
print(f"Country Code: {country_code}")
print(f"Default Accept-Language: {accept_language}")
