
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from myapp.models import Base

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Setup database connection
    engine = engine_from_config(settings, 'sqlalchemy.')
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)

    # Example route
    def my_view(request):
        session = Session()
        result = session.execute("SELECT * FROM my_table")
        session.close()
        return {'data': result.fetchall()}

    config.add_route('my_view', '/my_view')
    config.add_view(my_view, route_name='my_view')

    return config.make_wsgi_app()
