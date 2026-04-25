
premium_pizzas = [
    "Supreme Cheese", "The Legendary pizza", "Pentakill supreme",
    "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"
]
gourmet_pizzas = [
    "Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", 
    "BBQ Chicken", "Hellfire"
]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "selected_pizzas": 0,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def get_customer_name():
    while True:
        customer_name = input("Please enter your name: ")
        if customer_name:
            return customer_name
        print("Error: You must enter something!")

def get_delivery_address():
    while True:
        delivery_address = input("Please enter your delivery address: ")
        if delivery_address:
            return delivery_address
        print("Error: You must enter something!")

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number: "))
            if phone_number >= 1000000:
                return phone_number
            else:
                print("Phone number must be at least 7 digits long.")
        except ValueError:
            print("Phone number must be an integer only (no letters).")

def get_num_pizzas():
    while True:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
            if 0 < num_pizzas <= 5:
                return num_pizzas
            print('Invalid Input. Please choose a number between 1 and 5.')
        except ValueError:
            print('Invalid Input. Please enter a valid number.')

def pizza_list(num_pizzas):
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")
    print('\nEnter "next" to move on.\n')

    for _ in range(num_pizzas):
        while True:
            selected = input('Select Your Premium Pizza (or type "next"): ')
            if selected.lower() == 'next':
                break
            try:
                selected = int(selected)
                if 1 <= selected <= len(premium_pizzas):
                    pizza_dict['num_premium_pizzas'] += 1
                    break
                print('Invalid Input.')
            except ValueError:
                print('Invalid Input.')

def user_info():
    while True:
        choice = input("Press 1 for delivery, press 2 for pickup: ")
        if choice == "1":
            delivery_address = get_delivery_address()
            return delivery_address
        elif choice == "2":
            return None  # For pickup, no additional info
        else:
            print("Invalid choice! Please select 1 or 2.")

def main():
    customer_name = get_customer_name()
    phone_number = get_phone_number()
    num_pizzas = get_num_pizzas()
    delivery_address = user_info()
    pizza_list(num_pizzas)

    # Display summary
    summary = [customer_name, phone_number, delivery_address, num_pizzas]
    print("User Info:", summary)

if __name__ == "__main__":
    main()
