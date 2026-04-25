
import pika
import time

def main():
    # Set up connection and channel
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue
    queue_name = 'my_queue'
    channel.queue_declare(queue=queue_name, durable=True)

    while True:
        # Use basic_get to poll for messages
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            # A message was retrieved
            print(f"Received: {body.decode()}")
            # Acknowledge the message
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        else:
            # No messages available
            print("No messages in queue, checking again...")

        # Sleep for a while before polling again
        time.sleep(1)

    # Close connection (this line won't be reached in the above loop)
    connection.close()

if __name__ == "__main__":
    main()
