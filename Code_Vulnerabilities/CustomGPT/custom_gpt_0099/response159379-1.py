
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False  # Or however you want to implement equality

    def __hash__(self):
        return hash((self.__class__,))  # Provide an appropriate hash implementation

# Example usage
if __name__ == "__main__":
    obj1 = MyClass()
    obj2 = MyClass()
    print(obj1 == obj2)  # Outputs: False
    print(hash(obj1))     # Outputs the hash value
