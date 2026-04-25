
#!/usr/bin/python -3

class MyClass(object):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, MyClass):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)

# Example usage
if __name__ == "__main__":
    obj1 = MyClass(5)
    obj2 = MyClass(5)
    obj3 = MyClass(6)

    print(obj1 == obj2)  # True
    print(obj1 == obj3)  # False
    print(hash(obj1) == hash(obj2))  # True
