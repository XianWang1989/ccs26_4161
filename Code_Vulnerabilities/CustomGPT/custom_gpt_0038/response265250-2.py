
from pyramid.config import Configurator
from postgresql import attach

def main(global_config, **settings):
    # Set environment variable (if required)
    os.environ['DATABASE_URL'] = 'pq://username:password@localhost:5432/db_name'

    config = Configurator(settings=settings)

    # Attach to the database
    db_url = os.environ['DATABASE_URL']
    db = attach(db_url)

    # Example of querying the database
    @config.route('/')
    def my_view(request):
        with db.xact():
            result = db.prepare("SELECT * FROM my_table")()
        return {'results': result}

    return config.make_wsgi_app()
