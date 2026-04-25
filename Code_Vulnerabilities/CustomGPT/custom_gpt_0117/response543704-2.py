
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@cache.cached(timeout=300, key_prefix='user_data')
def fetch_user_data():
    r = session.get('http://myanimelist.net/malappinfo.php?u=doomcat55&status=all&type=anime')
    r.raise_for_status()
    return User(r.text)

def get_xml(f): 
    @wraps(f)
    def wrap():
        user = fetch_user_data()  # Use cached version
        response = f(user)
        return response
    return wrap
