
import pika
import time

def main():
    # Set up connection parameters
    connection_params = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    # Specify the queue we want to consume from
    queue_name = 'my_queue'
    channel.queue_declare(queue=queue_name, durable=True)

    try:
        while True:
            # Use basic_get to fetch a message without blocking
            method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

            # Check if a message was received
            if method_frame:
                print(f"Received message: {body.decode()}")
            else:
                print("No messages available. Waiting...")

            # Sleep for a short time to avoid overwhelming the RabbitMQ server
            time.sleep(1)

    except KeyboardInterrupt:
        print("Exited by user.")

    finally:
        connection.close()

if __name__ == '__main__':
    main()
