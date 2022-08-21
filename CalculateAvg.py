"Write a program to calculate average of numbers. Get the numbers from user until user enters 0."
number = 1
count = 0
total = 0
while (number != 0):
    number = int(input("enter: "))
    if (number != 0):  #if number is not equals to 0 
        total = total + number   #total carries the entered numbers
        count += 1   #incrementing the count for each loop
    else:
        break # if entered number is 0 the loop is break
if(count > 0): 
    print("Average is ", (total/(count)))

