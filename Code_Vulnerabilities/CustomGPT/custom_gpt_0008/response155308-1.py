
import pika
import time

def main():
    # Establish connection to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue from which we will consume messages
    queue_name = 'my_queue'
    channel.queue_declare(queue=queue_name)

    try:
        while True:
            # Use basic_get to check for messages
            method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

            if method_frame:
                print("Received message:", body.decode())
            else:
                print("No messages available, waiting...")

            # Sleep for a short while to avoid busy waiting
            time.sleep(1)

    except KeyboardInterrupt:
        print("Stopping consumer...")

    finally:
        # Clean up and close connection
        connection.close()

if __name__ == "__main__":
    main()
