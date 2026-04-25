
import requests

# Sample mapping of country codes to common Accept-Language and Accept-Charset
country_language_map = {
    "US": {"Accept-Language": "en-US,en;q=0.9", "Accept-Charset": "utf-8"},
    "FR": {"Accept-Language": "fr-FR,fr;q=0.9", "Accept-Charset": "iso-8859-1,utf-8;q=0.8"},
    "DE": {"Accept-Language": "de-DE,de;q=0.9", "Accept-Charset": "utf-8"},
    "RU": {"Accept-Language": "ru-RU,ru;q=0.9", "Accept-Charset": "windows-1251"},
    # Add more mappings as necessary
}

def get_country_code(ip):
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()
    return data.get("countryCode")

def get_default_accept_headers(ip):
    country_code = get_country_code(ip)
    return country_language_map.get(country_code, {"Accept-Language": "en", "Accept-Charset": "utf-8"})

# Example usage
ip_address = "8.8.8.8"  # Replace with the actual IP address
headers = get_default_accept_headers(ip_address)
print(headers)  # Outputs the default headers based on the IP's country code
