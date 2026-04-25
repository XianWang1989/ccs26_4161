
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return True  # Example condition for equality
        return False

    def __hash__(self):
        return hash(type(self))  # Or a more specific hashing logic

# Example usage
if __name__ == '__main__':
    obj1 = MyClass()
    obj2 = MyClass()

    print(obj1 == obj2)  # This will use the __eq__ method
    print(hash(obj1))    # This will use the __hash__ method
