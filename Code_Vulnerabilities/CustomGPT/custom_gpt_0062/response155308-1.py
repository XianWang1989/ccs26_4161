
import pika
import time

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue (ensure it exists)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Retrieve a message without blocking
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:  # If a message is retrieved
            print(f"Received message: {body.decode()}")
        else:
            print("No messages available.")

        # Sleep for a short time to avoid tight loop
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    connection.close()
