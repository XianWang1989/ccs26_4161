
import pika
import time

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='your_queue_name')

    while True:
        method_frame, header_frame, body = channel.basic_get(queue='your_queue_name', auto_ack=True)
        if method_frame:
            print(f"Received message: {body.decode()}")
        else:
            print("No messages, checking again...")
        time.sleep(1)  # Polling interval

    connection.close()

if __name__ == "__main__":
    main()
