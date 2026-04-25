
import socket

def test_connection():
    try:
        # Create a socket using IPv4 (AF_INET) family
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Example URL to connect; replace with your target
        host = 'example.com'
        port = 80
        sock.connect((host, port))
        print('Connection Successful')
    except Exception as e:
        print(f'Connection Failed: {e}')
    finally:
        sock.close()

test_connection()
