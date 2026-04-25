
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", 
                  "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", 
                  "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", 
                  "BBQ Chicken", "Hellfire"]

# Store user information
user_info = {}

def customer_name():
    while True:
        try:
            name = str(input("Please enter your name: "))
            if name.isalpha():  # Ensure name doesn't contain numbers
                user_info['name'] = name
                break
            else:
                print("Error: Name cannot contain numbers.")
        except Exception:
            print("Error: You must enter a valid name.")

def delivery_details():
    while True:
        try:
            address = str(input("Please enter your delivery address: "))
            if address:  # Ensure address is not empty
                user_info['address'] = address
                break
        except Exception:
            print("Error: You must enter a valid address.")

def phone_input():
    while True:
        try:
            phone_number = int(input("Please enter your phone number:\n\t"))
            if phone_number > 999999:  # Example: phone number should be at least 7 digits
                user_info['phone'] = phone_number
                break
            else:
                print("Error: Phone number must be at least 7 digits long.")
        except ValueError:
            print("Error: Phone number must be an integer only.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
            if num_pizzas < 1 or num_pizzas > 5:
                print('Invalid Input: Choose a number between 1 and 5.')
        except ValueError:
            print('Error: Invalid input, please enter a number.')

    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f'{i}. {pizza}')

    selected_pizzas = []
    for i in range(num_pizzas):
        while True:
            try:
                selection = int(input('Select your Premium Pizza (enter number): '))
                if 1 <= selection <= len(premium_pizzas):
                    selected_pizzas.append(premium_pizzas[selection - 1])
                    break
                else:
                    print('Invalid Input: Please select a valid pizza number.')
            except ValueError:
                print('Error: Invalid input, please enter a number.')

    print("You have selected the following pizzas:")
    for pizza in selected_pizzas:
        print(f"- {pizza}")

# Main function to control the flow
def main():
    customer_name()
    phone_input()
    delivery_details()
    pizza_list()

    print("\nUser Info Summary:")
    print(user_info)

# Start the program
main()
