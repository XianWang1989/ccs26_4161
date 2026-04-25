
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
    obj1 = MyClass(10)
    obj2 = MyClass(10)
    obj3 = MyClass(20)

    print(obj1 == obj2)  # True, same value
    print(obj1 == obj3)  # False, different value
