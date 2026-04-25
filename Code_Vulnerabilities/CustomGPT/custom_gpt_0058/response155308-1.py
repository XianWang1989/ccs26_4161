
import pika
import time

def main():
    # Set up the connection parameters
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue (make sure it exists)
    queue_name = 'your_queue_name'
    channel.queue_declare(queue=queue_name)

    try:
        while True:
            # Try to get a message from the queue
            method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

            if method_frame:
                print(f"Received message: {body.decode()}")
            else:
                print("No messages available. Waiting...")

            # Wait before checking again
            time.sleep(1)  # Adjust this value as needed for your use case
    finally:
        connection.close()

if __name__ == "__main__":
    main()
