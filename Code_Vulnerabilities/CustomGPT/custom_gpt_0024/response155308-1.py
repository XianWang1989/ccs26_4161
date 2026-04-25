
import pika
import time

def main():
    # Set up connection and channel
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue (make sure it exists)
    queue_name = 'my_queue'
    channel.queue_declare(queue=queue_name, durable=True)

    try:
        while True:
            # Use basic_get to check for messages
            method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

            # Check if a message was received
            if method_frame:
                print(f"Received message: {body.decode()}")
            else:
                print("No messages available.")

            # Sleep for a bit before checking again
            time.sleep(1)

    except KeyboardInterrupt:
        print("Stopping the consumer.")
    finally:
        connection.close()

if __name__ == '__main__':
    main()
