
import pika
import time

def main():
    # Set up the connection parameters
    connection_params = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    # Declare the queue
    queue_name = 'my_queue'
    channel.queue_declare(queue=queue_name)

    try:
        while True:
            # Use basic_get to check for messages
            method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)
            if method_frame:
                # If there's a message, print it
                print(f"Received message: {body.decode()}")
            else:
                # No messages available
                print("No messages available, waiting...")
            time.sleep(1)  # Wait before checking again
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        connection.close()

if __name__ == '__main__':
    main()
