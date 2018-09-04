# function to create list of numbers from user inout
def createList():
    list = []
    counter = 1
    while counter < 16:
        list.append(getInput(counter))
        counter = counter + 1
    
    squareNumbers(list)

# function to get squares of numbers
def squareNumbers(list):
    squares = {}

    for number in list:
        squares[number] = number*number

    print(squares)

# function to get user input
def getInput(count):
    print("this is input number %d" %count)
    number = input()
    number = int(number)
    return number



print("This is a dictionary of 15 numbers")
createList()



