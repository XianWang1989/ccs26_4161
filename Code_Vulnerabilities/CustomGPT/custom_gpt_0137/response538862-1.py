
class ExampleClass:
    def first_method(self):
        print("This is the first method.")
        self.second_method()

    def second_method(self):
        print("This is the second method.")
        self.third_method()

    def third_method(self):
        print("This is the third method.")

# Example usage
example = ExampleClass()
example.first_method()
