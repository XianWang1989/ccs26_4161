
import pika
import time

# Establish connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
queue_name = 'test_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)
        if method_frame:
            print("Received message:", body.decode())
        else:
            print("No message available. Checking again...")
        time.sleep(1)  # Poll every second
except KeyboardInterrupt:
    print("Consumer stopped.")
finally:
    connection.close()
