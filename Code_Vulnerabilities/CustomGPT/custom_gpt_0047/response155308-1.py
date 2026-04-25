
import pika
import time

# Establish connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (make sure it matches the producer's queue)
channel.queue_declare(queue='my_queue')

try:
    while True:
        # Try to get one message from the queue
        method_frame, header_frame, body = channel.basic_get(queue='my_queue', auto_ack=True)

        if method_frame:
            print("Received message:", body.decode('utf-8'))
        else:
            print("Waiting for messages...")

        # Sleep briefly to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped by user")

finally:
    connection.close()
