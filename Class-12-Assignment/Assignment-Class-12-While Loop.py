# Assignment-Class-12-While Loop-Ainur

list = []
lstNumber = int(input("How many number you want in the list:"))

start = 0
while start < lstNumber:  #
    number = int(input("Enter The numbers: "))  # To take input
    list.append(number)                         # To insert the input in the list
    start = start + 1                           # For looping increment
print("List Numbers are: ",list)                #

start = 0                                       # Starting point of iteration
while start < lstNumber:                        # While loop condition
    if list[start] % 10 == 0:                   # If condition for checking divisible by 10
        print("Numbers divisible by 10 are: ",list[start])
#    elif list[start] % 10 != 0:
#        print("No number is divisible by 10")
    elif list[start] > 120:                      # Else condition for checking greater than 120
        print("Loop breaked as inputed number is greater than 120")
        break
#    else:
        print("Number inserted to list, No number is divisible by 10 & Greater than 120")
    start = start+1                              #

