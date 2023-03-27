# Assignment-Class-12-While Loop-Ainur

# List Declaration
list = []

# Take user input of how many object/indexes will be in list
lstNumber = int(input("How many number you want in the list:"))

# Starting point of loop
start = 0
# Ending point of loop - List er index kotogula/list e koyta value ache
# end = len(list)

# While loop condition
while start < lstNumber:  #
    number = int(input("Enter The numbers: "))  # To take input
    list.append(number)                         # To insert the input in the list
    start = start + 1                           # For looping increment
print("List Numbers are: ",list)                #

# Display divisable by 10
index = 0                                       # Starting point of iteration
while index < lstNumber:                        # While loop condition
    if list[index] % 10 == 0:                   # If condition for checking divisible by 10
        print("Numbers divisible by 10 are: ",list[index])
#    elif list[index] % 10 != 0:
#        print("No number is divisible by 10")
    elif list[index] > 120:                      # Else condition for checking greater than 120
        print("Loop breaked as inputed number is greater than 120")
        break
#    else:
        print("Number inserted to list, No number is divisible by 10 & Greated than 120")
    index = index+1                              #

