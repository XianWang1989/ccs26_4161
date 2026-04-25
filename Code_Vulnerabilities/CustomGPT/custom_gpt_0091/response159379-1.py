
#!/usr/bin/python3

class MyClass(object):
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False  # or your actual equality logic here

    def __hash__(self):
        return hash(id(self))  # or any other hash logic based on the object's state

# Example usage
if __name__ == "__main__":
    a = MyClass()
    b = MyClass()
    print(a == b)  # Should print False
