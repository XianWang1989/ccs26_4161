
# Ensure db connection pooling is set
db = DAL('mysql://username:password@localhost/dbname', pool_size=10)

# A function to perform optimized queries
def get_data():
    query = '''
        SELECT TIMESTAMPDIFF(...) AS 'duration',
               ...
        FROM ... AS ris
        JOIN ... as sd ON ris.... = sd....
        WHERE ris.... != '0000-00-00 00:00:00'
        AND ris.... &gt;= '2010-8-15'
        AND ris.... &lt;= '2014-8-22';
    '''
    raw_data = db.executesql(query, as_dict=True)
    return raw_data

# Call the function
data = get_data()
