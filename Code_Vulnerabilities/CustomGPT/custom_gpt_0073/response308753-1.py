
# Example of a parameterized query
query = (db.ris.odate >= '2010-08-15') & (db.ris.odate <= '2014-08-22')
raw_data = db(query).select(db.ris.odate, db.ris.service)
