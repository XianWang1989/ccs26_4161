
import logging
from pyramid.config import Configurator

def main():
    config = Configurator()

    # Example of programmatically configuring logging
    logging.config.fileConfig('logging.ini')

    # Your other Pyramid configuration here
    return config.make_wsgi_app()

if __name__ == '__main__':
    app = main()
    # Run your app...
