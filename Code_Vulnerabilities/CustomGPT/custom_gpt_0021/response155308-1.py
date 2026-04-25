
import pika
import time

# Configure the connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue you want to consume from
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Attempt to get a message from the queue
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            # If a message is received, process it
            print(f"Received message: {body.decode()}")
            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            # No message received, can perform other tasks
            print("No messages available, checking again...")

        # Sleep to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping the consumer...")
finally:
    # Close the connection
    connection.close()
