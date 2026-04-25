
import pika
import time

# Establish connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Use basic_get to poll for messages
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            print("Received message:", body)

            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print("No messages available, checking again...")

        # Sleep for a short time before polling again
        time.sleep(1)

except KeyboardInterrupt:
    print("Polling stopped.")

finally:
    # Clean up and close the connection
    connection.close()
