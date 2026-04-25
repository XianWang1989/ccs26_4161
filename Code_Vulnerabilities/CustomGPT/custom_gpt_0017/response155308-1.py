
import pika
import time

# Set up connection and channel
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (ensure it exists)
channel.queue_declare(queue='my_queue')

try:
    while True:
        # Try to get a message from the queue
        method_frame, header_frame, body = channel.basic_get('my_queue', auto_ack=True)

        if method_frame:
            print(f"Received message: {body.decode()}")
        else:
            print("No messages in the queue, checking again...")

        # Sleep for a while before polling again
        time.sleep(1)

except KeyboardInterrupt:
    print("Polling stopped.")

finally:
    # Cleanup
    connection.close()
