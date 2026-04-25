
import pika
import time

def main():
    # Set up the connection and channel
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue (ensure it exists)
    channel.queue_declare(queue='your_queue_name')

    while True:
        # Use basic_get to fetch messages without blocking
        method_frame, header_frame, body = channel.basic_get(queue='your_queue_name')

        # Check if a message was received
        if method_frame:
            print("Received message:", body.decode())
            # Acknowledge the message
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        else:
            print("No messages available, sleeping...")

        # Sleep before polling again to avoid busy-waiting
        time.sleep(1)

    # Close the connection (this line won't be reached in this loop)
    connection.close()

if __name__ == '__main__':
    main()
