# Take a list of 5 numbers as input.
# Sort them in ascending order.
# Then reverse the order.
# Print both results.
# Hint: Use sort() and reverse()

# numbers = [5,4,3,2,1]
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)


# Take two lists of numbers.
# Merge them into one list.
# Sort the combined list.
# Hint: Use extend() and sort().

num1 = [1,4,5]
num2 = [7,3,1]
num1.extend(num2)
print(num1)
num1.sort()
print(num1)