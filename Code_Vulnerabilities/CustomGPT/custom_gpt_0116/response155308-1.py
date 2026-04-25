
import pika
import time

def main():
    # Set up the connection to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='your_queue_name')  # Declare your queue

    while True:
        # Use basic_get to check for messages
        method_frame, header_frame, body = channel.basic_get(queue='your_queue_name', auto_ack=True)

        if method_frame:
            print("Received message:", body.decode())
        else:
            print("No messages available.")

        # Sleep for a short duration to avoid busy waiting
        time.sleep(1)

    # Clean up
    connection.close()

if __name__ == "__main__":
    main()
