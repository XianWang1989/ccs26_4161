
import pika
import time

# Setup connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue (make sure it exists)
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Use basic_get to check for messages
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            print(f"Received message: {body.decode()}")
        else:
            print("No messages in queue.")

        # Sleep for a bit to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Polling stopped.")

finally:
    channel.close()
    connection.close()
