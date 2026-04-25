
import pika
import time

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare the queue
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Non-blocking check for messages
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            # If a message is available, process it
            print("Received message:", body.decode())
        else:
            # No message available
            print("No messages in the queue. Checking again in 1 second...")

        # Sleep for a while before checking again
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping the consumer...")

finally:
    # Close connection
    connection.close()
