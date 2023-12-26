# used a recursion to print all the numbers leading to 1. +
def validation(num):
    if num == 1:
        return num
    else:
        print(collatz(num))
        return validation(collatz(num))


# does the necessary maths conditions and calculations
def collatz(number):
    if number % 2 == 0:
        number = number // 2
        return number
    elif number % 2 == 1:
        number = 3 * number + 1
        return number


#checkpoint stage for valid inputs
def valid_inputs(rand):
    try:
        validation(int(rand))
    except ValueError:
        print("Must Enter an Integer.")


#main function
rand = input('Enter number:')
valid_inputs(rand)
