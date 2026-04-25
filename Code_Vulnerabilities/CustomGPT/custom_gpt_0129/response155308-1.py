
import pika
import time

# Set up connection parameters
connection_params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue (make sure the queue exists)
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Attempt to get a message from the queue
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            # If we got a message, process it
            print(f"Received message: {body.decode()}")
        else:
            # No message was available
            print("No messages available, waiting...")

        # Sleep for a short period to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    connection.close()
