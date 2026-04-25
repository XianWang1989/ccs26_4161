
import pika
import time

# Establish connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (ensure it exists)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

# Polling loop to check for messages
while True:
    method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

    if method_frame:
        print("Received message:", body.decode())
    else:
        print("No messages available.")

    # Sleep for a short time to avoid busy waiting
    time.sleep(1)

# Close the connection (not reached in this example but good practice)
# connection.close()
