# Input two strings. Output is both strings merged . Eg - input1 = ABCD, input 2 = 1234. Output = A1B2C3D4
firstInput = input("enter the string: ")     #ABCD
secondInput = input("enter the string: ")      #1234

finalOutput = ""
if(len(firstInput)<len(secondInput)):                   #if the first input is greater than secondInput
    for Index in range (0, len(firstInput)):            #for loops in run for 0, firstInput
        finalOutput += firstInput[Index]                #finalOutput is decleared as empty string initialy and store each of the firstInput characters to it
        finalOutput += secondInput[Index]               #and adding the secondinput to the finalOutput
else:                                                      # in else part
    for Index in range (0, len(secondInput)):           # the secondInput lenght is greater than the firstInput so the loop tuns for secondInput
       finalOutput += firstInput[Index]                  #storing the each characters of the firstInput in finalOutput
       finalOutput += secondInput[Index]                   #storing the each characters of the secondInput in finalOutput
print(finalOutput)                      #A1B2C3D4
