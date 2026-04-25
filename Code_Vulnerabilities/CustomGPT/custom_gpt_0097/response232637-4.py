
def main():
    name = input('Please Enter your question: ').lower()

    modules = [MODULE1, MODULE2]

    for module in modules:
        module.run()  # Call the run function of each module
        # Add logic here if you want to break
