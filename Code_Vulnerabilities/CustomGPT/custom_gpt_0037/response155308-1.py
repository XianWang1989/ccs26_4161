
import pika
import time

def main():
    # Set up the connection parameters
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue (make sure it exists)
    queue_name = 'my_queue'
    channel.queue_declare(queue=queue_name)

    try:
        while True:
            # Use basic_get to poll the queue
            method_frame, header_frame, body = channel.basic_get(queue=queue_name)

            if method_frame:
                print(f"Received message: {body.decode()}")
                # Acknowledge the message
                channel.basic_ack(method_frame.delivery_tag)
            else:
                print("No messages in the queue. Waiting...")

            # Sleep for a bit before checking again
            time.sleep(1)

    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        # Close the connection
        connection.close()

if __name__ == "__main__":
    main()
