
def optimized_query():
    # Prepare your SQL query here
    query = """
        SELECT TIMESTAMPDIFF(...) AS 'duration',
        TIMESTAMPDIFF(...) - INTERVAL 1 HOUR, TIMESTAMP(...) + INTERVAL CAST(...) AS 'timediff',
        ris.ODATE as 'date', CONCAT(...) as 'service'
        FROM ... AS ris
        JOIN ... as sd on ris.... = sd....
        WHERE ris.... != '0000-00-00 00:00:00'
          AND ris.... >= '2010-8-15'
          AND ris.... <= '2014-8-22'
    """

    # Example using prepared statements
    db.execute('SET @my_param = %s', ('2014-8-22',))
    raw_data = db.executesql(query, as_dict=True)

    return raw_data

# Example function call
if __name__ == "__main__":
    result = optimized_query()
    print(result)
