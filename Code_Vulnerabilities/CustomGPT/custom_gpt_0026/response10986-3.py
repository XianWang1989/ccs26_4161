
def get_default_headers(ip_address):
    country_code = get_country_code(ip_address)
    if country_code in country_preferences:
        accept_language, accept_charset = country_preferences[country_code]
        return {
            'Accept-Language': accept_language,
            'Accept-Charset': accept_charset
        }
    return {
        'Accept-Language': 'en',
        'Accept-Charset': 'UTF-8'
    }  # Fallback to default values
