
import pika
import time

# Connect to RabbitMQ server
def create_connection():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    return connection, channel

# Main function to consume messages
def consume_messages():
    connection, channel = create_connection()

    # Declare the queue (make sure it exists)
    queue_name = 'my_queue'
    channel.queue_declare(queue=queue_name)

    try:
        while True:
            # Use basic_get to check for messages without blocking
            method_frame, header_frame, body = channel.basic_get(queue=queue_name)

            if method_frame:
                # Process the message
                print(f"Received message: {body.decode()}")
                # Acknowledge the message
                channel.basic_ack(delivery_tag=method_frame.delivery_tag)
            else:
                print("No messages available. Waiting...")

            # Delay to avoid busy waiting
            time.sleep(1)  # Adjust the sleep duration as needed
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        connection.close()

if __name__ == "__main__":
    consume_messages()
