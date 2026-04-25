
import requests

# Function to get the country code based on IP
def get_country_code(ip):
    response = requests.get(f"https://ipapi.co/{ip}/json/").json()
    return response.get('country')

# Common Accept-Language settings by country
country_language_map = {
    'US': 'en-US,en;q=0.9',
    'FR': 'fr-FR,fr;q=0.9',
    'DE': 'de-DE,de;q=0.9',
    'RU': 'ru-RU,ru;q=0.9',
    'CN': 'zh-CN,zh;q=0.9',
    # Add more mappings as needed
}

# Function to get default Accept-Language header
def get_accept_language_header(ip):
    country_code = get_country_code(ip)
    return country_language_map.get(country_code, 'en-US,en;q=0.9')  # default if not found

# Example usage
if __name__ == "__main__":
    ip_address = '8.8.8.8'  # Example IP
    accept_language = get_accept_language_header(ip_address)
    print(f"Default Accept-Language for {ip_address}: {accept_language}")
