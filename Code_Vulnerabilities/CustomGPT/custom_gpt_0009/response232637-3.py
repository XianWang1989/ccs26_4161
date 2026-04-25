
from package import MODULE1, MODULE2  # Import all relevant modules

name = input('Please Enter your question: ').lower()

# List of module checks to run
module_checks = [
    MODULE1.check_color_question,
    MODULE2.check_car_question,
    # Add additional modules here...
]

# Iterate through module checks
for check in module_checks:
    result = check(name)
    if result:
        print(result)
        break  # Stop checking once a match is found
