
import requests
import geocoder

# Example IP address (you can replace this with the user's IP)
ip_address = "8.8.8.8"

# Get country code from IP address
g = geocoder.ip(ip_address)
country_code = g.country

# Define common languages and charsets for some countries
country_preferences = {
    'US': {'Accept-Language': 'en-US,en;q=0.9', 'Accept-Charset': 'utf-8'},
    'RU': {'Accept-Language': 'ru-RU,ru;q=0.9', 'Accept-Charset': 'windows-1251'},
    'FR': {'Accept-Language': 'fr-FR,fr;q=0.9', 'Accept-Charset': 'utf-8'},
    'DE': {'Accept-Language': 'de-DE,de;q=0.9', 'Accept-Charset': 'utf-8'},
    # Add more countries as needed
}

# Determine default headers based on country code
default_headers = country_preferences.get(country_code, {'Accept-Language': 'en', 'Accept-Charset': 'utf-8'})

print(f"Default headers for IP {ip_address} (Country: {country_code}):")
print(default_headers)
