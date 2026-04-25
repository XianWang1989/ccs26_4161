
import logging

logging.basicConfig(level=logging.INFO)

class ExampleClass:
    def first_method(self):
        logging.info("Navigating to first_method")
        print("This is the first method.")

    def second_method(self):
        logging.info("Navigating to second_method")
        print("This is the second method.")

    def third_method(self):
        logging.info("Navigating to third_method")
        print("This is the third method.")

# Usage
example = ExampleClass()
example.first_method()
example.second_method()
example.third_method()
