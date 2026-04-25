
import pika
import time

def main():
    # Set up the connection to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue (make sure it exists)
    channel.queue_declare(queue='my_queue')

    while True:
        # Check for messages in the queue
        method_frame, header_frame, body = channel.basic_get('my_queue')

        if method_frame:
            # A message was received, process it
            print("Received message:", body)
            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print("No messages available, checking again...")

        # Sleep for a short period before checking again
        time.sleep(1)

    # Close the connection (not reached in this example)
    connection.close()

if __name__ == "__main__":
    main()
