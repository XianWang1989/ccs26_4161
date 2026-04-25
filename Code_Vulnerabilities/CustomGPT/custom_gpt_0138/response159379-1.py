
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return True  # or your own logic
        return NotImplemented

    def __hash__(self):
        return hash((self.__class__,))  # or your own hash logic

# Example usage
if __name__ == "__main__":
    obj1 = MyClass()
    obj2 = MyClass()
    print(obj1 == obj2)  # This will call __eq__
    print(hash(obj1))    # This will call __hash__
