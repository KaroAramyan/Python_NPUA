
def sum_of_elements(numbers, exclude_negative=False):
 
    if exclude_negative:
        numbers = [num for num in numbers if num >= 0]
    return sum(numbers)

# Input from the user
user_input = input("Enter a list of numbers separated by spaces (e.g., '1 2 3 -4 5 -6'): ")
user_numbers = [float(num) for num in user_input.split()]

exclude_negative_input = input("Do you want to exclude negative numbers? (yes or no): ")
exclude_negative = exclude_negative_input.lower() == "yes"

# Calculate and print the sum of elements
result = sum_of_elements(user_numbers, exclude_negative)
print(f"Sum of the elements (excluding negatives: {exclude_negative}): {result}")

