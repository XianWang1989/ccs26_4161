
import pika
import time

# Function to consume messages from RabbitMQ
def consume_messages(queue_name):
    # Set up connection parameters
    connection_params = pika.ConnectionParameters('localhost')

    # Establish connection and create a channel
    with pika.BlockingConnection(connection_params) as connection:
        channel = connection.channel()

        # Declare the queue (make sure it exists)
        channel.queue_declare(queue=queue_name, durable=True)

        while True:
            # Poll for messages without blocking
            method_frame, header_frame, body = channel.basic_get(queue=queue_name)

            if method_frame:
                # Message received, process it
                print(f"Received message: {body.decode()}")

                # Acknowledge message
                channel.basic_ack(delivery_tag=method_frame.delivery_tag)
            else:
                # No message, sleep for a short duration before polling again
                print("No messages available. Retrying...")
                time.sleep(1)

# Usage
if __name__ == "__main__":
    consume_messages('your_queue_name')
