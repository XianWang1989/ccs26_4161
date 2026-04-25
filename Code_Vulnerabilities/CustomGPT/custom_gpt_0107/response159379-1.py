
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False  # Define your equality logic here

    def __hash__(self):
        return hash((self.__class__,))  # Customize hash as needed

# Example usage
if __name__ == "__main__":
    obj1 = MyClass()
    obj2 = MyClass()
    print(obj1 == obj2)  # Calls obj1.__eq__(obj2)
