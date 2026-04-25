
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data
dates = pd.date_range('2021-01-01', periods=100)
data = np.random.randn(100, 6)  # Random returns for six stocks
df2 = pd.DataFrame(data, index=dates, columns=['AAPL', 'MSFT', 'DELL', 'MS', 'BAC', 'C'])

# Calculate cumulative returns
df2 = ((1 + df2.pct_change()).cumprod() - 1).fillna(0)

# Plotting
df2.plot()
plt.title('Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.grid()
plt.show()
