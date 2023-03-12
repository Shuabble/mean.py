# Joshua Mikael P. Diñoso
# PostLab - 1 Contribution
# Programming Problem 1 - Mean Function

# Mean function, length of number list will be determined using python's inbuilt length function,
# and the sum of all numbers will be determined using python's inbuilt sum function.
# Function will return calculated mean value.
def meanCalculation(numbers):
    listLength = len(numbers)
    summation = sum(numbers)
    mean = summation/listLength
    return mean


print('\n')
# Ask the user for a list of numbers.
number_string = input("Enter a list of numbers separated by commas: ")
# Split each number input by a comma.
number_list = [int(num) for num in number_string.split(',')]
print('\n')
# Show the list of numbers that the user has inputted.
print("Number list: ", number_list)
# Call the mean function to calculate the mean of the given number list.
mean = meanCalculation(number_list)
print("\n")
print("The calculated mean is: ", mean)  # Show the calculated mean.
