
import pika
import time

def main():
    # Set up the connection to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue (make sure the queue exists)
    channel.queue_declare(queue='my_queue')

    try:
        while True:
            # Use basic_get() to check for messages
            method_frame, header_frame, body = channel.basic_get('my_queue')

            # If a message was received
            if method_frame:
                print("Received message:", body.decode())
                # Acknowledge the message
                channel.basic_ack(method_frame.delivery_tag)
            else:
                print("No messages in the queue. Checking again...")

            # Sleep before the next check
            time.sleep(1)  # Adjust the sleep time as needed

    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        # Clean up the connection
        connection.close()

if __name__ == "__main__":
    main()
