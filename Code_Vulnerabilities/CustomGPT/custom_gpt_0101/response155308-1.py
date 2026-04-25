
import pika
import time

# Establishing the connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='your_queue_name')

def poll_messages():
    while True:
        method_frame, header_frame, body = channel.basic_get('your_queue_name')

        if method_frame:
            print("Received message:", body)
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print("No messages available. Checking again...")

        time.sleep(1)  # Sleep for a second before checking again

try:
    poll_messages()
finally:
    connection.close()
