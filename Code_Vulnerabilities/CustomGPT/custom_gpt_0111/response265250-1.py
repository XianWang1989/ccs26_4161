
import os
from wsgiref.simple_server import make_server
from your_application import app  # Import your Pyramid app

if __name__ == "__main__":
    os.environ['DATABASE_URL'] = 'postgresql://username:password@localhost:5432/db_name'
    app.run()
