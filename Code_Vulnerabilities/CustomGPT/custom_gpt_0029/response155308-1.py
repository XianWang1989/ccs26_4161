
import pika
import time

def main():
    # Establish connection to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue from which we will consume messages
    channel.queue_declare(queue='my_queue', durable=True)

    try:
        while True:
            # Check for messages without blocking
            method_frame, header_frame, body = channel.basic_get(queue='my_queue', auto_ack=True)

            if method_frame:
                # A message was retrieved
                print(f"Received message: {body.decode()}")
            else:
                # No messages available, can perform other tasks or wait
                print("No messages available. Waiting...")

            # Sleep for a short time to avoid busy looping
            time.sleep(2)

    except KeyboardInterrupt:
        print("Consumer stopped.")

    finally:
        # Cleanup
        connection.close()

if __name__ == "__main__":
    main()
