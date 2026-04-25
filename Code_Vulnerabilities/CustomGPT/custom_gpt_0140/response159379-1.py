
#!/usr/bin/python -3

class MyClass(object):    
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False

    def __hash__(self):
        return hash(id(self))

# Example usage
if __name__ == "__main__":
    a = MyClass()
    b = MyClass()
    print(a == b)  # Output: False
