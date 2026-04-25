
def foo(input_list):
    def backtrack(index, current):
        if index == len(input_list):
            result.append(current[:])
            return
        # Choose positive
        current.append(abs(input_list[index]))
        backtrack(index + 1, current)
        # Choose negative
        current[-1] = -abs(input_list[index])
        backtrack(index + 1, current)
        current.pop()  # Backtrack

    result = []
    backtrack(0, [])
    return result
