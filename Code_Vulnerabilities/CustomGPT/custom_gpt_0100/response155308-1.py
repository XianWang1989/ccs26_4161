
import pika
import time

# Connection parameters
connection_params = pika.ConnectionParameters('localhost')  # Adjust host as needed

# Establishing connection and channel
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue you want to consume from (make sure it exists)
queue_name = 'your_queue'
channel.queue_declare(queue=queue_name, durable=True)

try:
    while True:
        # Attempt to get a message from the queue
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            print(f"Received message: {body.decode()}")
            # Process the message here
        else:
            print("No messages available. Waiting...")

        # Wait before polling again to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping consumer...")

finally:
    connection.close()
