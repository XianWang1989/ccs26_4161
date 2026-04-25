
import numpy as np
import pandas as pd

a = [10, 30, 12.5, 70, 76, 90, 96, 55, 44.5, 67.8, 76, 88]

bins = np.arange(0, 101, 10)
hist, bin_edges = np.histogram(a, bins=bins)

bin_data = pd.DataFrame({'bins': bin_edges[:-1], 'data': hist})
print(bin_data.to_string(index=False))
