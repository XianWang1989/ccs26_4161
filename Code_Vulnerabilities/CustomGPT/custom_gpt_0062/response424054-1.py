
def get_number_of_people():
    while True:
        try:
            num_of_people = int(input('Enter the number of people: '))
            break
        except ValueError:
            print("\nPlease make sure you key in number only! \n\tand please do not leave blank!")

    print("\nIs there any of these persons present?:")
    print("\tA. Disabled")
    print("\tB. 65-years-old and above")
    print("\tC. None for both A. and B.")

get_number_of_people()
