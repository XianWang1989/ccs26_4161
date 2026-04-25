
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return False  # Customize your equality logic here
        return NotImplemented

    def __hash__(self):
        return hash(id(self))  # Or any other hash logic relevant to your class

# Example usage
if __name__ == "__main__":
    obj1 = MyClass()
    obj2 = MyClass()

    print(obj1 == obj2)  # This will return False
    print(hash(obj1))    # This will print the hash of obj1
