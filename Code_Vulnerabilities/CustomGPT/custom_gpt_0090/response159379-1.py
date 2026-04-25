
#!/usr/bin/python3

class MyClass(object):    
    def __eq__(self, other):
        return False

    def __hash__(self):
        return id(self)  # or return a relevant integer

# Example usage
if __name__ == "__main__":
    obj1 = MyClass()
    obj2 = MyClass()
    print(obj1 == obj2)  # Should print: False
    print(hash(obj1))    # Will produce a hash value
