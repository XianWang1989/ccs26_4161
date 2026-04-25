
import pika
import time

def main():
    # Set up the connection and channel
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue
    queue_name = 'your_queue_name'
    channel.queue_declare(queue=queue_name)

    while True:
        # Try to get a message
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        # Check if a message was received
        if method_frame:
            print("Received message:", body.decode())
            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print("No messages in the queue.")

        # Sleep for a while before checking again
        time.sleep(1)

    # Close the connection (this line would not be reached in this example)
    connection.close()

if __name__ == '__main__':
    main()
