
import pandas as pd

# Check data types in chunks
def check_dtypes_in_chunks(file_path, chunk_size=1000):
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        print(chunk.dtypes)

check_dtypes_in_chunks('leads.csv')
