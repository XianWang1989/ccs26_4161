
class FirstClass:
    def method(self):
        print("Method in FirstClass")

class SecondClass(FirstClass):
    def method(self):
        print("Method in SecondClass")
        super().method()  # Calls the method from FirstClass

# Usage
obj = SecondClass()
obj.method()
