
# Ensure proper connection pooling (if applicable)
db = DAL('mysql://username:password@localhost/dbname', pool_size=10)

def fetch_data(query):
    # Query execution
    try:
        raw_data = db.executesql(query, as_dict=True)
    except Exception as e:
        print(f"Error: {e}")
        return None
    return raw_data

# Use the function
query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration', 
           TIMESTAMPDIFF(...) - INTERVAL 1 HOUR, 
           ris.ODATE as 'date', 
           CONCAT(...) as 'service' 
    FROM ... AS ris 
    JOIN ... AS sd on ris.... = sd.... 
    WHERE ris.... != '0000-00-00 00:00:00' 
      AND ris.... >= '2010-8-15' 
      AND ris.... <= '2014-8-22'
"""

# Fetch data and print
raw_data = fetch_data(query)
print(raw_data)
