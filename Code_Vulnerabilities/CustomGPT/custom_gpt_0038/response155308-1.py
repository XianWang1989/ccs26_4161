
import pika
import time

def main():
    # Set up the connection and channel
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue (make sure it exists)
    queue_name = 'your_queue_name'
    channel.queue_declare(queue=queue_name)

    try:
        while True:
            # Fetch a message without blocking
            method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

            if method_frame:
                print("Received message:", body.decode())
            else:
                print("No messages available.")

            # Sleep for a short time to prevent busy waiting
            time.sleep(1)

    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        connection.close()

if __name__ == "__main__":
    main()
