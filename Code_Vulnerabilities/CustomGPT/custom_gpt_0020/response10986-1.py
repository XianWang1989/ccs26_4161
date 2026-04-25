
import requests

# Function to determine the default language and charset based on country code
def get_default_language_and_charset(ip_address):
    # Geolocation API endpoint (replace with your preferred service)
    api_url = f"https://ipapi.co/{ip_address}/json/"

    # Making a request to the API
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        country_code = data.get('country_code', '').upper()

        # Define a mapping of country codes to default language and charset
        country_language_charset = {
            'US': ('en-US', 'utf-8'),
            'FR': ('fr-FR', 'utf-8'),
            'RU': ('ru-RU', 'windows-1251'),
            'DE': ('de-DE', 'utf-8'),
            'CN': ('zh-CN', 'utf-8'),
            # Add more countries as needed
        }

        # Get the default language and charset for the detected country code
        default_language, default_charset = country_language_charset.get(country_code, ('en', 'utf-8'))

        return default_language, default_charset
    else:
        print("Error fetching data from the geolocation service.")
        return None, None

# Example usage
ip = '8.8.8.8'  # Replace with the desired IP address
language, charset = get_default_language_and_charset(ip)
print(f"Default Accept-Language: {language}, Default Accept-Charset: {charset}")
