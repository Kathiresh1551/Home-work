# Input a string. Print first and last char, add a comma, then print second and last but first char and so on.
# eg - input ABCD1234 , output - A4,B3,C2,D1. 
# Hint - use only one for loop. 

inputString = input("enter the string: ")           #getting input      #kathir & kathiresh
reversedString = ""                                 #initialy reversedString is declear as empty staring
finalOutput = ""                                    #initialy finalOutput is declear as empty staring
for revIndex in range (len(inputString)-1, -1, -1): #get the inputString in reverse order
    reversedString += inputString[revIndex]         #push that in the decleared empty string that is reversedString    ===> rihtak, hserihtak
if (len(inputString) % 2 == 0):                     #if the lenght of the inputString is even 
    for char in range(0, int(len(inputString)/2)):  #for in is run between 0 to the half of the inputString     
        finalOutput += inputString[char]            #and stored the each inputSting of the word in the finalOutput    ===>finaloutput=kat
        finalOutput += reversedString[char] + ","   #this is to store the characters that is in reverse order         ===>finaloutput=kr,ai,th
else:
    for char in range(0, int(len(inputString)/2)):  #if the inputString is odd
        finalOutput += inputString[char]               #same process showed  in the if statement                      ===>finaloutput=kath
        finalOutput += reversedString[char] + ","                                                             #       ===>finaloutput=hser
    finalOutput += inputString[int(len(inputString)/2)] #additionly the missword in between is also added to the finalOutput   ===>finalOutput=kh,as,te,hr,i
print(finalOutput)


'''
OUTPUT:

enter the string: KATHIR
KR,AI,TH,


enter the string: KATHIRESH
KH,AS,TE,HR,I

'''
