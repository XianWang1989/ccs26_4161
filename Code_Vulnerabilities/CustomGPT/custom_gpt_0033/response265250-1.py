
from pyramid.config import Configurator
from pyramid.response import Response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Database connection
    db_url = 'postgresql://username:password@localhost:5432/db_name'
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    @config.route('/')
    def index(request):
        session = Session()
        # Your database logic here
        return Response('Hello World!')

    return config.make_wsgi_app()
