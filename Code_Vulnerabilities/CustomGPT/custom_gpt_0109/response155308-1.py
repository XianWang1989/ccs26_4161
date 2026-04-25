
import pika
import time

# Define connection parameters
connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

# Declare the queue (ensure it exists)
channel.queue_declare(queue='my_queue')

try:
    while True:
        # Use basic_get to check for messages
        method_frame, header_frame, body = channel.basic_get(queue='my_queue', auto_ack=True)

        if method_frame:
            print(f"Received message: {body.decode()}")
        else:
            print("No messages available, checking again...")

        # Sleep for a while before the next check
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping consumer...")
finally:
    connection.close()
