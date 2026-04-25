
# Initialize DAL with connection pooling
db = DAL('mysql://username:password@host/database_name', pool_size=10)

# Example SQL query
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration', ... 
FROM your_table AS ris 
JOIN second_table AS sd ON ris.your_column = sd.your_column 
WHERE ris.your_date_column >= '2010-08-15' 
AND ris.your_date_column <= '2014-08-22'";
"""

# Running the query
try:
    db.begin()  # Start transaction for better performance if running multiple queries
    raw_data = db.executesql(query, as_dict=True)
    db.commit()  # Commit transaction
except Exception as e:
    db.rollback()  # Rollback on error
    print(f"An error occurred: {e}")
finally:
    db.close()  # Ensure to close the connection

# Processing raw data
print(raw_data)
