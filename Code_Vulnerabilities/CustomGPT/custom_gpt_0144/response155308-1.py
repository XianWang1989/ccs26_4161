import pika
import time

# Set up the connection and channel
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue to ensure it exists
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name, durable=True)

try:
    while True:
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)
        if method_frame:
            print("Received message:", body.decode())
        else:
            print("No message available, checking again in 1 second...")
            time.sleep(1)
except KeyboardInterrupt:
    print("Stopped polling.")
finally:
    connection.close()
