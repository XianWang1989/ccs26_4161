
import pika
import time

# Set up connection parameters
connection_params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Use basic_get to check for messages
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            print(f"Received message: {body.decode()}")
            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print("No messages available.")

        # Sleep for a while before checking again
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping the consumer.")

finally:
    connection.close()
