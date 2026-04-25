
import pika
import time

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare the queue (make sure the queue exists)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Attempt to retrieve a message from the queue
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            # Process the message
            print(f"Received message: {body.decode()}")
            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print("No messages available. Checking again...")

        # Sleep for a short duration to avoid busy-waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping consumer.")

finally:
    connection.close()
