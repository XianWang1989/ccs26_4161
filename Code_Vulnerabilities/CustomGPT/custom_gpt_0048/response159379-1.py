
#!/usr/bin/python -3

class MyClass(object):    
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False  # Change this to your comparison logic as needed

    def __hash__(self):
        return hash((self.__class__,))  # Return a constant or relevant hash value

# Example usage
if __name__ == "__main__":
    obj1 = MyClass()
    obj2 = MyClass()
    print(obj1 == obj2)  # This will now work without warnings
