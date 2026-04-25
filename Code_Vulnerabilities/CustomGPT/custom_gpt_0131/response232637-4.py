
from package.MODULE1 import handle_question as handle_color_question
from package.MODULE2 import handle_question as handle_car_question
from package.MODULE3 import handle_question as handle_food_question

def main():
    question = input('Please Enter your question: ').lower()

    # Create a list of handler functions from different modules
    handlers = [handle_color_question, handle_car_question, handle_food_question]

    # Iterate through handlers to find a match
    for handler in handlers:
        handler(question)

if __name__ == "__main__":
    main()
