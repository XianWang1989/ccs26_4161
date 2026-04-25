
import pika
import time

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (make sure it exists)
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Use basic_get to check for messages
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            print("Received message:", body)
        else:
            print("No messages available.")

        # Sleep for a short duration to limit resource usage
        time.sleep(1)

except KeyboardInterrupt:
    print("Receiver stopped.")

finally:
    # Clean up and close connection
    connection.close()
