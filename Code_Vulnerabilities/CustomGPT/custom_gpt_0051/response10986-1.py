
import requests

# Dictionary to map country codes to Accept-Language and Accept-Charset
country_headers = {
    "US": {"Accept-Language": "en-US,en;q=0.9", "Accept-Charset": "UTF-8, ISO-8859-1;q=0.8"},
    "RU": {"Accept-Language": "ru-RU,ru;q=0.9", "Accept-Charset": "windows-1251, UTF-8;q=0.8"},
    "FR": {"Accept-Language": "fr-FR,fr;q=0.9", "Accept-Charset": "UTF-8, ISO-8859-1;q=0.8"},
    # Add more countries as needed
}

def get_country_code(ip_address):
    response = requests.get(f'http://ip-api.com/json/{ip_address}')
    data = response.json()
    if response.status_code == 200 and data['status'] == 'success':
        return data['countryCode']
    return None

def get_default_headers(ip_address):
    country_code = get_country_code(ip_address)
    if country_code and country_code in country_headers:
        return country_headers[country_code]
    return {"Accept-Language": "en", "Accept-Charset": "UTF-8"}

# Example usage
ip = '8.8.8.8'  # Replace with the actual IP
headers = get_default_headers(ip)
print(headers)
