
import pika
import time

class RabbitMQConsumer:
    def __init__(self, queue_name):
        self.queue_name = queue_name
        self.connection = None
        self.channel = None

    def connect(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name, durable=True)

    def consume(self):
        try:
            while True:
                method_frame, header_frame, body = self.channel.basic_get(queue=self.queue_name, auto_ack=True)

                if method_frame:
                    print(f"Received message: {body.decode()}")
                else:
                    print("No message available, waiting...")

                time.sleep(1)  # Add a small delay to avoid busy waiting
        except KeyboardInterrupt:
            print("Stopping consumer...")
        finally:
            self.close()

    def close(self):
        if self.connection:
            self.connection.close()

if __name__ == "__main__":
    consumer = RabbitMQConsumer('my_queue')
    consumer.connect()
    consumer.consume()
