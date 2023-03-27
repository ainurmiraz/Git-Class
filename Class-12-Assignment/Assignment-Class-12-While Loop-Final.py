# Assignment-Class-12-While Loop-Ainur

list = []                                                           # List Declaration
lstNumber = int(input("How many number you want in the list:"))     # List value/number input

start = 0                                       # Starting point of iteration
while start < lstNumber:                        # While Loop condition
    number = int(input("Enter The numbers: "))  # To take input
    list.append(number)                         # To insert the input in the list
    start = start + 1                           # For looping increment
print("List Numbers are: ", list)                #

start = 0                                       # Starting point of iteration
while start < lstNumber:                        # While loop condition
    if list[start] % 10 == 0:                   # If condition for checking divisible by 10
        print(list[start], "is divisible by 10")
    elif list[start] % 10 != 0:
        print(list[start],"is not divisible by 10")
    elif list[start] > 120:                      # Else condition for checking greater than 120
        print("Loop broken as inputted number is greater than 120")
        break
    else:
        print(list[start], "inserted to list, Its not divisible by 10 & Greater than 120")
    start = start+1                              #

