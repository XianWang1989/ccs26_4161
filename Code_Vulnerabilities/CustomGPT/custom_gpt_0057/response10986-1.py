
import requests

def get_country_and_headers(ip_address):
    response = requests.get(f"https://ipapi.co/{ip_address}/json/").json()
    country_code = response.get("country", "Unknown")

    default_headers = {
        'US': {'Accept-Language': 'en-US,en;q=0.9', 'Accept-Charset': 'UTF-8, *;q=0.5'},
        'DE': {'Accept-Language': 'de-DE,de;q=0.9', 'Accept-Charset': 'UTF-8, *;q=0.5'},
        'FR': {'Accept-Language': 'fr-FR,fr;q=0.9', 'Accept-Charset': 'UTF-8, *;q=0.5'},
        # Add more countries as needed
    }

    return default_headers.get(country_code, {'Accept-Language': 'en', 'Accept-Charset': 'UTF-8'})

ip_address = '8.8.8.8'  # Example IP address
headers = get_country_and_headers(ip_address)
print(headers)
