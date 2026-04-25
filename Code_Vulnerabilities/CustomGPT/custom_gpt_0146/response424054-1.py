
# Continuing from the previous code snippet
response = raw_input("Enter your response (A/B/C): ")

if response.upper() == 'A':
    print("Some disabled persons are present.")
elif response.upper() == 'B':
    print("Some persons aged 65 and above are present.")
elif response.upper() == 'C':
    print("No persons from both categories are present.")
else:
    print("Invalid option selected!")
