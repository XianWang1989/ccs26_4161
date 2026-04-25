
import pika
import time

# Setup connection and channel
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (make sure the queue exists)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name, durable=True)

try:
    while True:
        # Try to get a message from the queue
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            print("Received message:", body)
        else:
            print("No messages in queue.")

        # Sleep for a short period to avoid busy-waiting
        time.sleep(1)
except KeyboardInterrupt:
    print("Interrupted by the user.")
finally:
    channel.close()
    connection.close()
