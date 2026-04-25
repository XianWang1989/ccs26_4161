
import requests

# Function to get country code from IP
def get_country_code(ip):
    response = requests.get(f"https://ipapi.co/{ip}/json/")
    data = response.json()
    return data.get("country")

# Mapping of country codes to preferred language and charset
country_language_mapping = {
    "US": ("en-US", "UTF-8"),
    "FR": ("fr-FR", "UTF-8"),
    "DE": ("de-DE", "UTF-8"),
    "RU": ("ru-RU", "windows-1251"),
    "CN": ("zh-CN", "UTF-8"),
    # Add more country mappings as needed
}

# Function to get preferred Accept-Language and Accept-Charset
def get_accept_headers(ip):
    country_code = get_country_code(ip)
    if country_code in country_language_mapping:
        language, charset = country_language_mapping[country_code]
        return {
            "Accept-Language": language,
            "Accept-Charset": charset
        }
    return None

# Example Usage
ip_address = "8.8.8.8"  # Replace with the user's IP address
headers = get_accept_headers(ip_address)
if headers:
    print("Suggested headers:")
    print(headers)
else:
    print("Country code not found, using default headers.")
