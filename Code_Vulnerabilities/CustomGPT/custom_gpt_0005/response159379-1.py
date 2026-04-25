
#!/usr/bin/python3

class MyClass(object):    
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False  # Define your equality logic here

    def __hash__(self):
        return hash(id(self))  # Provide a hash implementation

# Example usage
if __name__ == "__main__":
    obj1 = MyClass()
    obj2 = MyClass()
    print(obj1 == obj2)  # Use the equality operator
    print(hash(obj1))    # Check the hash value
