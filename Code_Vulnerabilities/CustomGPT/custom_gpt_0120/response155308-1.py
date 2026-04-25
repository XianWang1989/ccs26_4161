
import pika
import time

# Set up RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue (make sure it's the same queue that sends messages)
channel.queue_declare(queue='your_queue_name')

try:
    while True:
        # Poll for messages
        method_frame, header_frame, body = channel.basic_get(queue='your_queue_name', auto_ack=True)

        if method_frame:
            print(f"Received message: {body.decode()}")
        else:
            print("No messages available. Checking again...")

        # Sleep for a while to avoid busy-waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Clean up and close connection
    connection.close()
