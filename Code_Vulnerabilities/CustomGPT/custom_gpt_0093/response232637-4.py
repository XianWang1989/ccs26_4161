
# main.py
from package import MODULE1, MODULE2, MODULE3

def main():
    question = input('Please enter your question: ').lower()

    modules = [MODULE1, MODULE2, MODULE3]

    for module in modules:
        response = module.handle_question(question)
        if response:
            print(response)
            break
    else:
        print('No module could handle your question.')

if __name__ == '__main__':
    main()
