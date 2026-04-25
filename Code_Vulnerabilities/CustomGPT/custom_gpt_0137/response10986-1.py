
import requests

def get_country_code(ip_address):
    """Get the country code from an IP address."""
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    data = response.json()
    return data.get("country", None)

def determine_accept_language(country_code):
    """Determine default Accept-Language header based on country code."""
    language_mapping = {
        "US": ("en-US", "UTF-8"),
        "GB": ("en-GB", "UTF-8"),
        "FR": ("fr-FR", "UTF-8"),
        "DE": ("de-DE", "UTF-8"),
        "CN": ("zh-CN", "GB18030"),
        "RU": ("ru-RU", "windows-1251"),
        # Add more mappings as needed
    }
    return language_mapping.get(country_code, ("en-US", "UTF-8"))  # Default to English if country not found

# Example usage
ip_address = "8.8.8.8"  # Replace this IP address with the user's IP
country_code = get_country_code(ip_address)

if country_code:
    accept_language, charset = determine_accept_language(country_code)
    print(f"Default Accept-Language: {accept_language}, Charset: {charset}")
else:
    print("Could not determine country code.")
