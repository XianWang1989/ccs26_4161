
import pika
import time

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare the queue (make sure the queue exists)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Use basic_get to check for messages
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            print("Received message:", body.decode())
            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print("No messages available, checking again...")

        # Sleep for a bit to prevent tight looping
        time.sleep(1)

except KeyboardInterrupt:
    print("Consuming stopped by user.")

finally:
    # Close the connection
    connection.close()
