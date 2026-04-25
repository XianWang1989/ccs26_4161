
class ExampleClass:
    def method_one(self):
        print("Method One")

    def method_two(self):
        self.method_one()
        print("Method Two")

    def method_three(self):
        self.method_two()
        print("Method Three")

# Instance creation
example = ExampleClass()

# Navigate through methods
example.method_three()
