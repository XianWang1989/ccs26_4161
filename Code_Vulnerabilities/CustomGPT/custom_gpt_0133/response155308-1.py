
import pika
import time

# Define connection parameters
connection_params = pika.ConnectionParameters('localhost')

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue from which you want to consume messages
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name, durable=True)

try:
    while True:
        # Use basic_get to check for messages
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            # A message is available
            print("Received message:", body.decode())
            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            # No messages available
            print("No messages. Checking again in 1 second...")

        time.sleep(1)  # Sleep for some time before checking again

except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Clean up and close the connection
    connection.close()
