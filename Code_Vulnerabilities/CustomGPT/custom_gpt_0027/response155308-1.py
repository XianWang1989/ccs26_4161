
import pika
import time

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue
    queue_name = 'my_queue'
    channel.queue_declare(queue=queue_name)

    try:
        while True:
            # Poll the queue for messages
            method_frame, header_frame, body = channel.basic_get(queue=queue_name)

            if method_frame:
                print(f"Received message: {body.decode()}")
                # Acknowledge the message
                channel.basic_ack(method_frame.delivery_tag)
            else:
                print("No message available.")

            # Sleep for a while to prevent tight loop
            time.sleep(1)

    except KeyboardInterrupt:
        print("Polling stopped.")
    finally:
        connection.close()

if __name__ == '__main__':
    main()
