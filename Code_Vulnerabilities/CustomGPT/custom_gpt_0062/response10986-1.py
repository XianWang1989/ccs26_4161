
import requests

# Function to get country code from IP
def get_country_code(ip):
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    data = response.json()
    return data.get('country')

# Mapping of country codes to Accept-Language and Accept-Charset
country_mapping = {
    'US': {'Accept-Language': 'en-US', 'Accept-Charset': 'UTF-8'},
    'RU': {'Accept-Language': 'ru-RU', 'Accept-Charset': 'windows-1251'},
    'CN': {'Accept-Language': 'zh-CN', 'Accept-Charset': 'GBK'},
    # Add more mappings as needed
}

def get_default_headers(ip):
    country_code = get_country_code(ip)
    if country_code in country_mapping:
        return country_mapping[country_code]
    else:
        return {'Accept-Language': 'en', 'Accept-Charset': 'UTF-8'}  # Default fallback

# Example usage
ip_address = '8.8.8.8'  # Replace with the target IP
headers = get_default_headers(ip_address)
print(headers)
