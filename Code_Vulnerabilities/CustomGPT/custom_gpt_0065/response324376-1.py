
import socket

def check_connection(request):
    try:
        # This will test the connection to an external server
        socket.create_connection(("example.com", 80))
        return HttpResponse("Connection successful!")
    except OSError as e:
        return HttpResponse(f"Connection failed: {e}")
