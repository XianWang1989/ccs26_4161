
import pika
import time

def main():
    # Setup connection
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue from which you want to consume
    channel.queue_declare(queue='your_queue_name')

    try:
        while True:
            # Use basic_get to check for messages
            method_frame, header_frame, body = channel.basic_get(queue='your_queue_name', auto_ack=True)

            if method_frame:
                print("Received message:", body)
            else:
                print("No messages in queue.")

            # Sleep for a while to avoid busy waiting
            time.sleep(1)

    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        connection.close()

if __name__ == "__main__":
    main()
