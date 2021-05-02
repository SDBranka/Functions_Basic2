
# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element). Example: countdown(5) should return [5,4,3,2,1,0]
print("---Countdown---")

def countdown(num):
    a_list = []
    for x in range(num, -1, -1):
        a_list.append(x)
    return a_list

number = 5
x = countdown(number)
print(x)


#Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.   Example: print_and_return([1,2]) should print 1 and return 2
print("---Print and Return---")

def print_and_return(a_list):
    for x in range(len(a_list)):
        if(x == 0):
            print(a_list[x])
    return a_list[x]

x = [1, 2]
print(print_and_return(x))


#First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.   Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
print("\n\n---First Plus Length---")

def first_plus_length(a_list):
    return a_list[0] + len(a_list)

x = [1,2,3,4,5]
print(first_plus_length(x))


#Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False. Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]     Example: values_greater_than_second([3]) should return False
print("\n\n---Values Greater than Second---")

def values_greater_than_second(a_list):
    new_list = []
    max = a_list[1]
    greater_vals = 0

    for v in a_list:
        if(v > max):
            new_list.append(v)
            greater_vals += 1
    
    print(greater_vals)
    return new_list

x = [5,2,3,2,1,4]
print(values_greater_than_second(x))

#This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.   Example: length_and_value(4,7) should return [7,7,7,7] Example: length_and_value(6,2) should return [2,2,2,2,2,2]
print("\n\n---This Length, That Value")

def length_and_value(size, value):
    new_list = []

    for x in range(size):
        new_list.append(value)

    return new_list

x = length_and_value(4, 7)
print(x)