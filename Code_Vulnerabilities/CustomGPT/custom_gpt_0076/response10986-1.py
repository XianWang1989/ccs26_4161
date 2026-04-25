
import requests

# Example mapping of country codes to Accept-Language and Accept-Charset
country_language_map = {
    "US": ("en-US,en;q=0.9", "UTF-8"),
    "RU": ("ru-RU,ru;q=0.9", "windows-1251"),
    "DE": ("de-DE,de;q=0.9", "UTF-8"),
    "FR": ("fr-FR,fr;q=0.9", "UTF-8"),
    # Add more countries as needed
}

def get_country_code(ip):
    """Retrieve the country code based on the IP address."""
    response = requests.get(f"https://ipapi.co/{ip}/country/")
    return response.text

def determine_language_and_charset(ip):
    """Determine the default Accept-Language and Accept-Charset based on IP."""
    country_code = get_country_code(ip)
    if country_code in country_language_map:
        return country_language_map[country_code]
    else:
        return ("en", "UTF-8")  # Default values if country not in map

# Example usage
ip_address = "8.8.8.8"  # Replace with the user's IP address
accept_language, accept_charset = determine_language_and_charset(ip_address)

print(f"Accept-Language: {accept_language}")
print(f"Accept-Charset: {accept_charset}")
