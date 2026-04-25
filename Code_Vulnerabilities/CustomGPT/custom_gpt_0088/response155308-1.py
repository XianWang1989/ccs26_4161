
import pika
import time

# Establish connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (make sure it exists)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Use basic_get to check for messages
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            print("Received message:", body.decode())
        else:
            print("No messages available. Checking again...")

        # Sleep for a short period before checking again
        time.sleep(1)

except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    connection.close()
