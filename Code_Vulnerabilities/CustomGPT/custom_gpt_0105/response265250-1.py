
import postgresql

def connect_to_database():
    try:
        # Replace with your database credentials
        db = postgresql.open('pq://username:password@localhost:5432/db_name')
        print("Connection successful!")
        return db
    except postgresql.exceptions.ClientCannotConnectError as e:
        print(f"Connection error: {e}")
    except postgresql.exceptions.PermissionError as e:
        print(f"Permission denied: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    connect_to_database()
