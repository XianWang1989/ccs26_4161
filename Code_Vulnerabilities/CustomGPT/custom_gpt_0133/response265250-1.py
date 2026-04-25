
import psycopg2
from psycopg2 import sql
from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='home', renderer='json')
def home_view(request):
    connection = None
    try:
        # Connect to your postgres DB
        connection = psycopg2.connect(
            dbname="db_name",
            user="username",
            password="password",
            host="localhost",
            port="5432"
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Execute a query
        cursor.execute("SELECT * FROM your_table;")
        records = cursor.fetchall()

        return {'data': records}

    except Exception as e:
        return Response(f"Error: {str(e)}", status=500)

    finally:
        if connection:
            cursor.close()
            connection.close()
