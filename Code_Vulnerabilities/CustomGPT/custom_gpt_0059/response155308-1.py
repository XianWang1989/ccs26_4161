
import pika
import time

# Establish connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name, durable=True)

while True:
    # Check for messages without blocking
    method_frame, header_frame, body = channel.basic_get(queue=queue_name)

    if method_frame:
        print(f"Received message: {body.decode()}")
        # Acknowledge the message
        channel.basic_ack(method_frame.delivery_tag)
    else:
        print("No messages available.")

    # Sleep for a short interval before the next check
    time.sleep(1)

# Close the connection (this line is never reached in this infinite loop)
connection.close()
