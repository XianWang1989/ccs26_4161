
import pika
import time

def main():
    # Define connection parameters to RabbitMQ server
    connection_params = pika.ConnectionParameters(host='localhost')

    # Establish a connection to RabbitMQ
    connection = pika.BlockingConnection(connection_params)

    # Create a channel
    channel = connection.channel()

    # Declare the queue from which to consume
    queue_name = 'my_queue'
    channel.queue_declare(queue=queue_name, durable=True)

    try:
        while True:
            # Use basic_get to retrieve a message without blocking
            method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

            if method_frame:
                # A message was received
                print(f"Received message: {body.decode()}")
            else:
                # No message received, you can handle idle time if necessary
                print("No message received, checking again...")

            # You can add a small sleep to avoid busy waiting
            time.sleep(1)

    except KeyboardInterrupt:
        print("Interrupted by user. Exiting...")

    finally:
        # Clean up and close connection
        connection.close()

if __name__ == '__main__':
    main()
