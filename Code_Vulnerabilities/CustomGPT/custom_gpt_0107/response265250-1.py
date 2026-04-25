
from pyramid.config import Configurator
import postgresql

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Database connection
    db = postgresql.open('pq://username:password@localhost:5432/db_name')

    @config.route('/')
    def index(request):
        result = db.query("SELECT * FROM your_table")
        return {'data': result}

    return config.make_wsgi_app()
