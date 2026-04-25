
from pyramid.config import Configurator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_db_session():
    DATABASE_URL = "postgresql+psycopg2://username:password@localhost:5432/db_name"
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    return Session()

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('home', '/')

    @config.view(route_name='home')
    def home_view(request):
        session = get_db_session()
        # Your database operations here
        return {'status': 'Database connection successful!'}

    return config.make_wsgi_app()
