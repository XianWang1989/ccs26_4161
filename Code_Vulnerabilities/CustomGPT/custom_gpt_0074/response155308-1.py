
import pika
import time

# Establishing a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue from which you want to consume messages
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name, durable=True)

try:
    while True:
        # Check for messages in the queue
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            # If a message is available, process it
            print("Received message:", body.decode())
            # Acknowledge the message after processing
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        else:
            # No messages available; wait a bit before checking again
            print("No messages available, checking again...")
            time.sleep(1)  # Adjust the sleep time as necessary

except KeyboardInterrupt:
    print("Consumer stopped.")
finally:
    # Clean up and close the connection
    connection.close()
