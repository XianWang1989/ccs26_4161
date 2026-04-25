
import pika
import time

def main():
    # Set up connection parameters
    connection_params = pika.ConnectionParameters('localhost')  # Change as necessary
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    # Declare the queue (make sure it exists)
    queue_name = 'your_queue_name'  # Replace with your queue name
    channel.queue_declare(queue=queue_name)

    try:
        while True:
            # Use basic_get to check for messages
            method_frame, header_frame, body = channel.basic_get(queue_name, auto_ack=True)

            if method_frame:
                print("Received message:", body.decode())
            else:
                print("No messages available")

            # Sleep for a short duration to avoid busy waiting
            time.sleep(1)

    except KeyboardInterrupt:
        print("Interrupted by user")

    finally:
        connection.close()

if __name__ == "__main__":
    main()
