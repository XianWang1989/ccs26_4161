
from pyramid.config import Configurator
import postgresql

def main(global_config, **settings):
    config = Configurator(settings=settings)
    db = postgresql.open('pq://username:password@localhost:5432/db_name')

    # Example database operation
    with db.transaction():
        news = db.prepare('SELECT * FROM your_table')()
        for item in news:
            print(item)

    return config.make_wsgi_app()
