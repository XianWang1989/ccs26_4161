
import pika
import time

def main():
    # Set up the connection and channel
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue (ensure it exists)
    queue_name = 'your_queue_name'
    channel.queue_declare(queue=queue_name, durable=True)

    try:
        while True:
            # Use basic_get to check for messages without blocking
            method_frame, header_frame, body = channel.basic_get(queue=queue_name)

            if method_frame:
                print("Received message:", body.decode())
                # Acknowledge the message
                channel.basic_ack(method_frame.delivery_tag)
            else:
                print("No messages available.")

            # Wait before polling again to avoid busy waiting
            time.sleep(1)

    except KeyboardInterrupt:
        print("Stopping consumer...")
    finally:
        # Clean up the connection
        connection.close()

if __name__ == "__main__":
    main()
