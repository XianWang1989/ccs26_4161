
import pika
import time

# Establish connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (make sure it exists)
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Attempt to get a message
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        # Check if a message was received
        if method_frame:
            print(f"Received message: {body.decode()}")
        else:
            print("No messages available, checking again...")

        # Sleep for a short period to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Interrupted by user.")

finally:
    # Clean up and close the connection
    channel.close()
    connection.close()
