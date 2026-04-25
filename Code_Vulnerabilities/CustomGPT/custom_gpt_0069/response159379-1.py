
#!/usr/bin/python -3

class MyClass(object):    
    def __eq__(self, other):
        # Define equality logic
        return isinstance(other, MyClass)

    def __hash__(self):
        # Return a hash value
        return hash("MyClass")

# Example usage
if __name__ == "__main__":
    obj1 = MyClass()
    obj2 = MyClass()
    print(obj1 == obj2)  # Should print: True
    print(hash(obj1))    # Print hash of obj1
