
import pika
import time

def main():
    # Set up connection to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Declare the queue (make sure it exists)
    channel.queue_declare(queue='my_queue')

    while True:
        # Use basic_get to check for messages
        method_frame, header_frame, body = channel.basic_get(queue='my_queue', auto_ack=True)

        if method_frame:
            print("Received message:", body.decode())
        else:
            print("No messages available, checking again...")

        # Sleep for a while to avoid busy waiting
        time.sleep(1)

if __name__ == "__main__":
    main()
