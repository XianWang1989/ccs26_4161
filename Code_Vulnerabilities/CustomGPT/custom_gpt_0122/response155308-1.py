
import pika
import time

# Function to create a connection and channel
def create_connection():
    parameters = pika.ConnectionParameters('localhost')  # Adjust as needed
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    return connection, channel

# Main polling loop
def main():
    connection, channel = create_connection()
    queue_name = 'your_queue_name'  # Specify your queue name

    try:
        while True:
            # Use basic_get to check for messages
            method_frame, header_frame, body = channel.basic_get(queue=queue_name)

            if method_frame:
                # Process the message
                print(f"Received message: {body.decode()}")
                channel.basic_ack(method_frame.delivery_tag)  # Acknowledge the message
            else:
                print("No messages available, waiting...")

            # Sleep briefly to avoid busy-waiting
            time.sleep(1)

    except KeyboardInterrupt:
        print("Polling stopped.")

    finally:
        connection.close()

if __name__ == "__main__":
    main()
