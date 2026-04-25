
import time

start_time = time.time()
raw_data = dbs.executesql(query, as_dict=True)
end_time = time.time()
print("Query executed in: {:.2f} seconds".format(end_time - start_time))
