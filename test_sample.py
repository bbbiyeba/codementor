# test_sample.py - Sample code for testing CodeMentor

def calculate_sum(numbers):
    """Calculate sum of numbers in a list."""
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    return total

def find_max(lst):
    """Find maximum value in a list."""
    max = lst[0]
    for num in lst:
        if num > max:
            max = num
    return max

# Test the functions
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(f"Sum: {calculate_sum(nums)}")
    print(f"Max: {find_max(nums)}")
    