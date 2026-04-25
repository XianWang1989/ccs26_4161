
max_num = None
while True:
    score = input("Enter a score (or type 'exit' to stop): ")
    if score.lower() == 'exit':
        break
    try:
        score_int = int(score)
        if max_num is None or score_int > max_num:
            max_num = score_int
    except ValueError:
        print("Please enter a valid integer.")

print("The highest score entered is:", max_num)
