
#!/usr/bin/python -3

class MyClass(object):    
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return False
        return NotImplemented

    def __hash__(self):
        return hash(id(self))

# Example usage
if __name__ == "__main__":
    a = MyClass()
    b = MyClass()
    print(a == b)  # Outputs: False
