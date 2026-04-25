
from package import module1, module2, module3

def main():
    name = input('Please Enter your question: ').lower()

    # Check each module
    if name in module1.play():
        module1.play()
    elif name in module2.play():
        module2.play()
    elif name in module3.play():
        module3.play()
    else:
        print("No matches found in any module.")

if __name__ == "__main__":
    main()
