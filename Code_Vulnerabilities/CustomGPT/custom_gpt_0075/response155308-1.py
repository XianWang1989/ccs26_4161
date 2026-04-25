
import pika
import time

def main():
    # Set up connection to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue (must match the producer)
    queue_name = 'my_queue'
    channel.queue_declare(queue=queue_name)

    try:
        while True:
            # Try to get a message without blocking
            method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

            if method_frame:
                # Message received
                print(f"Received message: {body.decode()}")
            else:
                # No message received
                print("No message available, checking again in 1 second.")

            # Delay before next poll to avoid busy waiting
            time.sleep(1)

    except KeyboardInterrupt:
        print("Polling stopped.")

    finally:
        # Clean up the connection
        connection.close()

if __name__ == "__main__":
    main()
