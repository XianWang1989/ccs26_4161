
# Measure a simple query time in web2py
import time
start_time = time.time()
db.executesql('SELECT 1')
print("Time taken:", time.time() - start_time)
