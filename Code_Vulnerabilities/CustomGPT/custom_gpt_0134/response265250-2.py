
def application(environ, start_response):
    import postgresql
    try:
        db = postgresql.open('pq://username:password@127.0.0.1:5432/db_name')
        # Example query
        result = db.query("SELECT * FROM your_table")
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [bytes(str(result), 'utf-8')]
    except Exception as e:
        start_response('500 Internal Server Error', [('Content-Type', 'text/plain')])
        return [bytes(f"Error: {str(e)}", 'utf-8')]
