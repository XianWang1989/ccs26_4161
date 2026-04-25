
import matplotlib.pyplot as plt

# Your frequency data in dictionary format
freq = {1: 1000, 2: 980, 4: 560, 40: 3, 41: 1, 43: 1}

# Create lists for the X and Y values
x_values = list(freq.keys())
y_values = list(freq.values())

# Create the bar chart
plt.bar(x_values, y_values, color='blue')

# Adding labels and title
plt.xlabel('Numbers')
plt.ylabel('Frequency')
plt.title('Bar Chart of Frequency Distribution')

# Display the plot
plt.show()
