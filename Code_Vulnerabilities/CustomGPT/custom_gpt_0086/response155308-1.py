
import pika
import time

# Set up the RabbitMQ connection and channel
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (make sure it matches the one used for sending messages)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Use basic_get to check for messages
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            # Process the message if available
            print(f"Received message: {body.decode()}")
        else:
            # No message received; you can add a delay to prevent busy-waiting
            print("No messages in the queue. Waiting...")

        # Sleep for a short duration before the next poll
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Clean up and close the connection
    connection.close()
