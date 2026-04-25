
import pika
import time

# Function to create a channel and connect to RabbitMQ
def create_connection():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='your_queue_name', durable=True)  # Declare the queue
    return connection, channel

# Main function to poll for messages
def poll_messages():
    connection, channel = create_connection()

    try:
        while True:
            # Try to get a message from the queue
            method_frame, header_frame, body = channel.basic_get('your_queue_name', auto_ack=True)

            if method_frame:
                # We received a message
                print(f"Received message: {body.decode()}")
            else:
                # No messages in the queue, do something else or wait
                print("No messages. Checking again in 1 second...")

            time.sleep(1)  # Sleep for a short duration before checking again

    except KeyboardInterrupt:
        print("Polling stopped by user.")
    finally:
        connection.close()

if __name__ == '__main__':
    poll_messages()
