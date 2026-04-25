
import pika
import time

# Set up connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue (make sure it exists)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Try to get a message non-blocking
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            print(f"Received message: {body.decode()}")
        else:
            print("No messages available, checking again...")

        # Sleep or do other work
        time.sleep(1)  # Adjust the interval as needed

except KeyboardInterrupt:
    print("Stopping the consumer...")

finally:
    connection.close()
