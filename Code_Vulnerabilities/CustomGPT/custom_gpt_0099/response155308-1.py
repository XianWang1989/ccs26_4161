
import pika
import time

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare your queue (make sure it exists)
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Use basic_get to check if there are messages
        method_frame, header_frame, body = channel.basic_get(queue_name)

        if method_frame:
            # There is a message
            print(f"Received message: {body.decode()}")
            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            # No message available
            print("No messages available.")

        # Sleep for a short duration to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping consumer.")
finally:
    connection.close()
