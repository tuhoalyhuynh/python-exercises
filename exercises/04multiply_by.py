# Write a method called `multiply_by` that takes a list and
# a number, and returns the list of numbers multiplied by that number.
#
# You'll want to apply your fundamental programming knowledge here.
# What are the pieces to this problem? You'll need to define a method,
# need a return statement, need a for loop to iterate over the array.
#
# Example method call:
#
# multiply_by([1, 2, 3], 5)
#
# > [5, 10, 15]

def multiply_by(num_list, multiple):
    multiple_list = []
    for num in num_list:
        new_num = int(num) * int(multiple)
        multiple_list.append(new_num)
    print(multiple_list)

multiply_by([1,2,3,4,5], 5)