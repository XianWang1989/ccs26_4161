
import requests

def get_country_from_ip(ip):
    try:
        response = requests.get(f"https://ipapi.co/{ip}/json/")
        data = response.json()
        return data.get("country", "")
    except Exception as e:
        print(f"Error fetching country: {e}")
        return None

def get_accept_language_and_charset(country_code):
    language_map = {
        'US': ('en-US', 'UTF-8'),
        'FR': ('fr-FR', 'ISO-8859-1'),
        'DE': ('de-DE', 'ISO-8859-1'),
        'RU': ('ru-RU', 'Windows-1251'),
        'CN': ('zh-CN', 'UTF-8'),
        # Add more mappings as needed
    }
    return language_map.get(country_code, ('en-US', 'UTF-8'))  # Default

def main():
    ip_address = '8.8.8.8'  # Replace with the user's IP
    country_code = get_country_from_ip(ip_address)

    if country_code:
        accept_language, charset = get_accept_language_and_charset(country_code)
        print(f"Country Code: {country_code}")
        print(f"Suggested Accept-Language: {accept_language}")
        print(f"Suggested Accept-Charset: {charset}")
    else:
        print("Could not determine country code.")

if __name__ == "__main__":
    main()
