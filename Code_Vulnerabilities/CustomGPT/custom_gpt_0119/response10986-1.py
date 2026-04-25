
import requests

# Sample mapping of country codes to preferred Accept-Language and Accept-Charset headers
country_preferences = {
    'US': ('en-US,en;q=0.5', 'utf-8'),
    'RU': ('ru-RU,ru;q=0.9', 'windows-1251'),
    'CN': ('zh-CN,zh;q=0.9', 'utf-8'),
    'DE': ('de-DE,de;q=0.9', 'utf-8'),
    # Add more mappings as needed
}

def get_country_code(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')
    data = response.json()
    return data.get('country')

def get_default_headers(ip_address):
    country_code = get_country_code(ip_address)
    if country_code in country_preferences:
        return country_preferences[country_code]
    else:
        return ('en-US', 'utf-8')  # Default fallback

# Example usage
user_ip = '134.201.250.155'  # Example IP address
accept_language, accept_charset = get_default_headers(user_ip)

print(f'Accept-Language: {accept_language}')
print(f'Accept-Charset: {accept_charset}')
