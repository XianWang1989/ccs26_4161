
from pyramid.config import Configurator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_db_connection():
    # Use TCP connection
    connection_string = "postgresql://username:password@127.0.0.1:5432/db_name"
    engine = create_engine(connection_string)

    # Create a new session
    Session = sessionmaker(bind=engine)
    return Session()

def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Example of using the database connection
    @config.route('/example')
    def example_view(request):
        session = get_db_connection()
        # Execute your query/logic here
        return {"message": "Connected!"}

    return config.make_wsgi_app()
