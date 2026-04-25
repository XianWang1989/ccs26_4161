
import requests

# Mapping of country codes to typical Accept-Language and Accept-Charset headers
country_headers = {
    'US': {
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Charset': 'UTF-8,ISO-8859-1;q=0.5'
    },
    'RU': {
        'Accept-Language': 'ru-RU,ru;q=0.9',
        'Accept-Charset': 'windows-1251,UTF-8;q=0.5'
    },
    'DE': {
        'Accept-Language': 'de-DE,de;q=0.9',
        'Accept-Charset': 'UTF-8,ISO-8859-1;q=0.5'
    },
    # Add more countries as needed
}

def get_country_code(ip_address):
    # Use an IP geolocation service to get the country code
    response = requests.get(f'https://ip-api.com/json/{ip_address}')
    data = response.json()
    return data['countryCode'] if 'countryCode' in data else None

def get_headers_for_ip(ip_address):
    country_code = get_country_code(ip_address)
    if country_code and country_code in country_headers:
        return country_headers[country_code]
    return {
        'Accept-Language': 'en;q=0.8',  # Default fallback
        'Accept-Charset': 'UTF-8;q=0.9'
    }

# Example usage
ip = '8.8.8.8'  # Replace with the actual IP address
headers = get_headers_for_ip(ip)
print(headers)
