
#!/usr/bin/python3

class MyClass(object):
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False  # Your custom equality logic here

    def __hash__(self):
        return hash(id(self))  # This returns a hash based on the object's id

# Example usage
if __name__ == "__main__":
    obj1 = MyClass()
    obj2 = MyClass()
    print(obj1 == obj2)  # Outputs: False
