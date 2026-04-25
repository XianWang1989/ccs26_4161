
import requests

# Example function to fetch country code from IP
def get_country_code(ip):
    response = requests.get(f"https://ipapi.co/{ip}/json/")
    if response.status_code == 200:
        return response.json().get("country")
    return None

# Mapping of country codes to default Accept-Language values
country_language_map = {
    "US": "en-US,en;q=0.5",
    "FR": "fr-FR,fr;q=0.9",
    "DE": "de-DE,de;q=0.8",
    "RU": "ru-RU,ru;q=0.7",
    "CN": "zh-CN,zh;q=0.9",
}

# Function to get default Accept-Language header based on country code
def get_default_accept_language(ip):
    country_code = get_country_code(ip)
    return country_language_map.get(country_code, "en-US,en;q=0.5")

# Example usage
ip_address = "8.8.8.8"  # Example IP address
default_accept_language = get_default_accept_language(ip_address)
print(f"Default Accept-Language for IP {ip_address}: {default_accept_language}")
