
import pika
import time

# Define the RabbitMQ connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue (make sure it exists)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name, durable=True)

try:
    while True:
        # Attempt to get a message from the queue
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            print(f"Received message: {body.decode()}")
            # Here you can add processing logic for the message
        else:
            print("No messages in the queue.")

        # Sleep for a short while to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping the consumer.")

finally:
    # Close the connection
    connection.close()
