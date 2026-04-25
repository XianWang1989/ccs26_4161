
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return False  # Modify this logic as needed
        return NotImplemented

    def __hash__(self):
        return hash(id(self))

# Example usage
if __name__ == "__main__":
    obj1 = MyClass()
    obj2 = MyClass()

    print(obj1 == obj2)  # Should return False
    print(hash(obj1))    # Should return a unique hash value
