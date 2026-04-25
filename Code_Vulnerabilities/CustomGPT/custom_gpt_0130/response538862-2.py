
import logging

logging.basicConfig(level=logging.INFO)

class Example:
    def method_one(self):
        logging.info("method_one called")
        print("This is method one.")

    def method_two(self):
        logging.info("method_two called")
        print("This is method two.")

# Usage
example = Example()
example.method_one()
example.method_two()
