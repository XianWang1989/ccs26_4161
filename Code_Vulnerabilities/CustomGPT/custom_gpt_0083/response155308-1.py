
import pika
import time

def main():
    # Set up connection parameters
    connection_params = pika.ConnectionParameters(host='localhost')
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    # Declare the queue
    queue_name = 'your_queue_name'
    channel.queue_declare(queue=queue_name, durable=True)

    try:
        while True:
            # Non-blocking retrieval of a message from the queue
            method_frame, header_frame, body = channel.basic_get(queue=queue_name)

            if method_frame:
                # A message was retrieved; acknowledge it
                print(f"Received: {body.decode()}")
                channel.basic_ack(delivery_tag=method_frame.delivery_tag)
            else:
                # No message available; you can use a sleep to avoid busy waiting
                print("No messages available. Checking again...")
                time.sleep(1)  # wait before checking again

    except KeyboardInterrupt:
        print("Stopping the consumer...")

    finally:
        channel.close()
        connection.close()

if __name__ == "__main__":
    main()
