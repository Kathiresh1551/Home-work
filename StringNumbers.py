# strNumber = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
number = str(input("enter the number: "))
errormesg = False
NaN = 0
for strNumber in range (0, len(number)):
    if(number[strNumber] == "1"):
        print(end="one")
        errormesg = False
    elif(number[strNumber] == "2"):
        print(end="two")
        errormesg = False
    elif(number[strNumber] == "3"):
        print(end="three")
        errormesg = False
    elif(number[strNumber] == "4"):
        print(end="four")
        errormesg = False
    elif(number[strNumber] == "5"):
        print(end="five")
        errormesg = False
    elif(number[strNumber] == "6"):
        print(end="six")
        errormesg = False
    elif(number[strNumber] == "7"):
        print(end="seven")
        errormesg = False
    elif(number[strNumber] == "8"):
        print(end="eight")
        errormesg = False
    elif(number[strNumber] == "9"):
        print(end="nine")
        errormesg = False
    elif(number[strNumber] == "0"):
        print(end="zero")
        errormesg = False
    else:
        NaN += 1
        break

    # print(end=number[strNumber])
if(NaN > 0):
    print("NaN")

