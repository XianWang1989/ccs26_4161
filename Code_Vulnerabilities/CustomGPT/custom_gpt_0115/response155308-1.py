
import pika
import time

def main():
    # Set up connection and channel
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue (make sure it exists)
    queue_name = 'your_queue_name'
    channel.queue_declare(queue=queue_name)

    while True:
        # Poll for messages
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            print("Received:", body.decode())
        else:
            print("No messages available.")

        # Sleep for a bit to avoid busy-waiting
        time.sleep(1)

    # Close the connection (this line won't be reached in this example)
    connection.close()

if __name__ == '__main__':
    main()
