# Input a string. 
# Print all the chars that are in Odd index - eg intput - abcd, output bd
# Print all the chars in the even index in reverse order - eg input abcd output ca


inputString = input("enter the string: ")      #getting the input string
startIndex = -1                                #declearing the start index as -1
print("odd")
for oddIndex in range (1, len(inputString), 2):  #loop is runs for the odd index so its is starts with 1
    print(inputString[oddIndex])                    #orinting the otuput of oddindex
print('-------------------------')
print("even")
if(len(inputString)%2 == 0):
    startIndex = len(inputString) -2                #if the lenth of the input string is even modifying the start index as lenght of the input string - 2
else:
    startIndex = len(inputString) -1                   #if the lenth of the input string is odd modifying the start index as lenght of the input string - 2
for evenIndex in range (startIndex, -1, -2):            #the loop is runs for startindex that is modified (started in the last index or second last) to last first
    # index(we need to have the first index value so the -1 is placed)
    print(inputString[evenIndex])
    
    
'''
enter the string: kathir
odd
a
h
r
-------------------------
even
i
t
k


enter the string: kathiresh
odd
a
h
r
s
-------------------------
even
h
e
i
t
k
'''
