
#!/usr/bin/python -3

class MyClass(object):    
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False  # Define your custom equality logic here

    def __hash__(self):
        # Return a hash value. You can use a fixed value or a unique identifier.
        return hash((self.__class__,))  # Example: hash based on class type

# Example usage
if __name__ == "__main__":
    obj1 = MyClass()
    obj2 = MyClass()
    print(obj1 == obj2)  # Output: False
    print(hash(obj1))     # Output: A hash value
