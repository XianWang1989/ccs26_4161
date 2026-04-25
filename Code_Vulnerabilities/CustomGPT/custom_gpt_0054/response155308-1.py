
import pika
import time

# Define a function to receive messages
def receive_messages(queue_name):
    # Establish a connection to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Declare the queue you want to consume from
    channel.queue_declare(queue=queue_name)

    while True:
        # Attempt to get a message from the queue
        method_frame, header_frame, body = channel.basic_get(queue_name, auto_ack=True)

        # Check if a message was retrieved
        if method_frame:
            print(f"Received message: {body.decode()}")
        else:
            print("No messages available, checking again...")

        # Sleep for a while before checking again
        time.sleep(2)

    # Close the connection (this part will not be reached in the above loop)
    connection.close()

# Usage example
if __name__ == '__main__':
    receive_messages('my_queue')
