
def foo(lst):
    # Helper function for recursion
    def generate(pos_neg, idx):
        if idx == len(lst):
            results.append(pos_neg[:])
            return

        # Add positive and negative possibilities for current number
        generate(pos_neg + [abs(lst[idx])], idx + 1)  # Positive
        generate(pos_neg + [-abs(lst[idx])], idx + 1) # Negative

    results = []
    generate([], 0)
    return results

# Example usage
print(foo([-4]))           # [[4], [-4]]
print(foo([1, 1]))        # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))       # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))    # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]
