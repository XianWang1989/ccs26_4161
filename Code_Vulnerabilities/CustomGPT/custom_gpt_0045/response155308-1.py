
import pika
import time

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue from which to receive messages
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Use basic_get to check if there are messages in the queue
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            print(f"Received message: {body.decode()}")
            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print("No messages in the queue. Checking again...")

        # Introduce a little delay to avoid hammering the server
        time.sleep(1)

except KeyboardInterrupt:
    print("Receiver stopped.")

finally:
    # Close the connection to RabbitMQ
    connection.close()
