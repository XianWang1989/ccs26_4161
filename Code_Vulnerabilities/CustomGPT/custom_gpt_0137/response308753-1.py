
# Assuming you are already inside a web2py controller

def run_query():
    # Enable SQL logging for debug purposes
    db.executesql("SET sql_mode='NO_BACKSLASH_ESCAPES';")
    db.executesql("SET FOREIGN_KEY_CHECKS=1;")

    # First execution that is slow
    query = """
        SELECT TIMESTAMPDIFF(...) AS 'duration',
               ... -- rest of your query
        FROM ... AS ris
        JOIN ... as sd on ris.... = sd....
        WHERE ris.... != '0000-00-00 00:00:00'
            AND ris.... != '0000-00-00 00:00:00'
            AND ris.... >= '2010-8-15'
            AND ris.... <= '2014-8-22'
    """

    # Run the query
    raw_data = db.executesql(query, as_dict=True)
    print(db._timings)  # Output timing information for debugging

    # Second execution which should be faster
    raw_data_again = db.executesql(query, as_dict=True)
    print(raw_data_again)

# Example of using the controller function
run_query()
