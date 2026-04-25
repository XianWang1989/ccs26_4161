
import pika
import time

# Establishing the connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare the queue (make sure it exists)
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Non-blocking get
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            print(f"Received message: {body.decode()}")
        else:
            print("No messages available.")

        # Sleep for a bit to avoid busy waiting
        time.sleep(1)

finally:
    connection.close()
