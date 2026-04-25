
import pika
import time

def main():
    # Set up connection and channel
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue to consume from
    channel.queue_declare(queue='my_queue')

    try:
        while True:
            # Use basic_get to check for messages
            method_frame, header_frame, body = channel.basic_get(queue='my_queue', auto_ack=True)

            if method_frame:
                print(f"Received message: {body.decode()}")
            else:
                print("No messages available, checking again...")

            # Add a short delay to avoid busy-waiting
            time.sleep(1)
    except KeyboardInterrupt:
        print("Polling stopped by user.")
    finally:
        connection.close()

if __name__ == '__main__':
    main()
