
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return False
        return NotImplemented

    def __hash__(self):
        return hash(id(self))  # or any other hash logic appropriate for your class

# Example usage
if __name__ == "__main__":
    obj1 = MyClass()
    obj2 = MyClass()
    print(obj1 == obj2)  # This will output: False
