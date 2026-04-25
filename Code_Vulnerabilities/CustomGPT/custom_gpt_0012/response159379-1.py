
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return True  # Implement your own logic for equality
        return False

    def __hash__(self):
        return hash(id(self))  # You can implement your own hash logic here

# Example usage:
if __name__ == "__main__":
    obj1 = MyClass()
    obj2 = MyClass()

    print(obj1 == obj2)  # This will now compare properly without warnings
    print(hash(obj1))    # This will call the custom __hash__ method
