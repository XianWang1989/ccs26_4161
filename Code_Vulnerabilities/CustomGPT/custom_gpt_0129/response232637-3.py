
from package import MODULE1, MODULE2

def main():
    question = input('Please Enter your question: ').lower()

    response = MODULE1.handle_color_question(question)
    if response:
        print(response)
    else:
        response = MODULE2.handle_car_question(question)
        if response:
            print(response)
        else:
            print("No relevant module found for the question.")

if __name__ == "__main__":
    main()
