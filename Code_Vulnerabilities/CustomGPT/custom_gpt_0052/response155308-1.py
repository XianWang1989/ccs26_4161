
import pika
import time

def main():
    # Set up connection parameters
    connection_params = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    # Declare the queue
    queue_name = 'my_queue'
    channel.queue_declare(queue=queue_name)

    while True:
        # Use basic_get to poll for messages
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            print("Received message:", body.decode())
        else:
            print("No messages available.")

        # Sleep for a while before polling again
        time.sleep(1)

    # Close the connection (not reached in this example)
    connection.close()

if __name__ == "__main__":
    main()
