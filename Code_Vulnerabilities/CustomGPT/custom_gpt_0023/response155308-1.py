
import pika
import time

def main():
    # Set up the connection and channel
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue (make sure it exists)
    queue_name = 'your_queue_name'
    channel.queue_declare(queue=queue_name, durable=True)

    try:
        while True:
            # Check for messages without blocking
            method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

            if method_frame:
                print("Received message:", body.decode())
            else:
                print("No messages available. Waiting...")

            # Sleep for a while before checking again
            time.sleep(1)

    except KeyboardInterrupt:
        print("Receiver stopped.")
    finally:
        connection.close()

if __name__ == "__main__":
    main()
