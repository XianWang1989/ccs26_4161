
import pika
import time

def setup_queue():
    # Establish a connection to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue to consume from (make sure it exists)
    channel.queue_declare(queue='my_queue', durable=True)

    return connection, channel

def poll_for_messages(channel):
    while True:
        # Try to get a message without blocking
        method_frame, header_frame, body = channel.basic_get(queue='my_queue', auto_ack=True)

        if method_frame:
            print("Received message: %r" % body)
        else:
            print("No messages available, checking again...")

        # Wait before polling again
        time.sleep(1)

if __name__ == "__main__":
    connection, channel = setup_queue()
    try:
        poll_for_messages(channel)
    except KeyboardInterrupt:
        print("Stopping consumer...")
    finally:
        connection.close()
