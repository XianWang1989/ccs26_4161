
import sqlite3

# Connect to your SQLite database (replace 'your_database.db' with your database file)
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Query the data (replace 'your_table' with your actual table name)
cursor.execute("SELECT * FROM your_table")
rows = cursor.fetchall()

# Create an HTML file and write the data
with open('output.html', 'w') as file:
    file.write('<html><head><title>Data Output</title></head><body>\n')
    file.write('<h1>Data from Database</h1>\n')
    file.write('<table border="1">\n')

    # Write headers
    file.write('<tr>')
    for column in cursor.description:
        file.write(f'<th>{column[0]}</th>')
    file.write('</tr>\n')

    # Write data rows
    for row in rows:
        file.write('<tr>')
        for item in row:
            file.write(f'<td>{item}</td>')
        file.write('</tr>\n')

    file.write('</table>\n</body></html>')

# Close the database connection
conn.close()

print("Data exported to output.html")
