
import pika
import time

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name, durable=True)

try:
    while True:
        # Use basic_get to fetch a message without blocking
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            print(f"Received message: {body.decode()}")
            # Process the message here
        else:
            print("No messages available, checking again...")

        # Sleep for a bit to avoid tight loop
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping consumer...")
finally:
    # Clean up and close connection
    connection.close()
