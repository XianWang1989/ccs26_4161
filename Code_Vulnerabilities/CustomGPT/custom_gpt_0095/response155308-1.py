
import pika
import time

def main():
    # Set up connection parameters
    connection_params = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    # Specify the queue you want to consume from
    queue_name = 'your_queue_name'
    channel.queue_declare(queue=queue_name)

    while True:
        # Use basic_get to check for messages
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            # A message was received
            print(f"Received message: {body.decode()}")
        else:
            # No message available, sleep a bit before checking again
            print("No messages available. Checking again in a second...")

        # Sleep to avoid busy-waiting
        time.sleep(1)

    # Clean up
    connection.close()

if __name__ == '__main__':
    main()
