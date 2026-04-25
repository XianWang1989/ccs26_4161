
premium_pizzas = [
    "Supreme Cheese", "The Legendary pizza", "Pentakill supreme", 
    "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", 
    "Vegetriano"
]
gourmet_pizzas = [
    "Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", 
    "BBQ Chicken", "Hellfire"
]

pizza_dict = {
    "premium_pizza_price": 8.50, 
    "gourmet_pizza_price": 5.00, 
    "num_premium_pizzas": 0, 
    "num_gourmet_pizzas": 0
}

def customer_name():
    name = ""
    while name == "":
        try:
            name = str(input("Please enter your name: "))
        except ValueError:
            print("Error: You must enter something! (cannot be a number)")
    return name

def delivery_details():
    address = ""
    while address == "":
        address = str(input("Please enter your delivery address: "))
    return address

def phone_number():
    phone = -1
    while phone < 0 or phone < 7:
        try:
            phone = int(input("Please enter your phone number (at least 7 digits): "))
        except ValueError:
            print("Phone number must be an integer only.")
    return phone

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")

    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    for _ in range(num_pizzas):
        select_pizza(premium_pizzas, "premium")
        select_pizza(gourmet_pizzas, "gourmet")

def select_pizza(pizza_list, pizza_type):
    while True:
        selected = input(f'Select Your {pizza_type.capitalize()} Pizza (or "next" to move on): ')
        if selected == 'next':
            break
        else:
            try:
                selected = int(selected) - 1
                if selected < 0 or selected >= len(pizza_list):
                    print('Invalid Input')
                else:
                    if pizza_type == "premium":
                        pizza_dict['num_premium_pizzas'] += 1
                    else:
                        pizza_dict['num_gourmet_pizzas'] += 1
            except ValueError:
                print('Invalid Input')

def main():
    name = customer_name()
    phone = phone_number()
    delivery = delivery_details()
    pizza_list()

    print("\nOrder Summary:")
    print(f"Customer Name: {name}")
    print(f"Phone Number: {phone}")
    print(f"Delivery Address: {delivery}")
    print(f"Total premium pizzas: {pizza_dict['num_premium_pizzas']}, Total gourmet pizzas: {pizza_dict['num_gourmet_pizzas']}")

if __name__ == "__main__":
    main()
