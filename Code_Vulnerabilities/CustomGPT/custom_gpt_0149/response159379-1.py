
#!/usr/bin/python3

class MyClass:
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return False
        return NotImplemented

    def __hash__(self):
        return hash(id(self))

# Example usage
if __name__ == "__main__":
    obj1 = MyClass()
    obj2 = MyClass()
    print(obj1 == obj2)  # Outputs: False
