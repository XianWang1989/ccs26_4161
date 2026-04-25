
# Example of a batched SQL execution
query1 = "SELECT * FROM table1;"
query2 = "SELECT * FROM table2;"

# Execute as a single transaction (if applicable)
with db.connection() as conn:
    with conn.cursor() as cursor:
        cursor.execute(query1)
        result1 = cursor.fetchall()

        cursor.execute(query2)
        result2 = cursor.fetchall()

# Process results
print(result1, result2)
