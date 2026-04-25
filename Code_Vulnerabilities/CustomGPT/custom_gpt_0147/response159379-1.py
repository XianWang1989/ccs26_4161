
#!/usr/bin/python -3

class MyClass(object):    
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False  # or any other comparison logic

    def __hash__(self):
        return hash(id(self))  # or any hash logic relevant to your class

# Example usage
if __name__ == "__main__":
    obj1 = MyClass()
    obj2 = MyClass()
    print(obj1 == obj2)  # Outputs: False
