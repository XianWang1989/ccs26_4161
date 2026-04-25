
import pandas as pd

# Sample data (replace with your database query)
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Create HTML file
html_output = df.to_html(index=False)

with open('output.html', 'w') as file:
    file.write(html_output)

print("HTML file generated successfully!")
