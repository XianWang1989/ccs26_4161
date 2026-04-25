
import pika
import time

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (make sure it exists)
channel.queue_declare(queue='my_queue')

while True:
    method_frame, header_frame, body = channel.basic_get(queue='my_queue')

    if method_frame:
        print(f"Received message: {body.decode()}")
        channel.basic_ack(method_frame.delivery_tag)
    else:
        print("No messages available. Checking again...")

    time.sleep(1)  # Wait for a second before checking again

# Close the connection when done
# connection.close()
