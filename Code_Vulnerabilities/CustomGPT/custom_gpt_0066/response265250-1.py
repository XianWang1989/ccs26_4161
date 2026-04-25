
import asyncpg
from pyramid.config import Configurator

async def database_connection(request):
    connection = await asyncpg.connect(user='username', password='password',
                                        database='db_name', host='127.0.0.1')
    return connection

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('home', '/')
    return config.make_wsgi_app()
