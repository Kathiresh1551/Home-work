# Print the level of the password security and if the password is acceptable
#     Weak - only alphabets or only numbers or only special chars
#     Ok - at least one alphabet, one number and one special char
#     strong - at least three alphabets, two numbers and one special char
#     Very strong - same as strong, but at least 16 count
#     All passwords must be at least 8 chars long.
inputPassword = input("Password: ")     
alphabets = 0
numbers = 0
specialChar = 0
for charIndex in range (0, len(inputPassword)):     #the loop is run between 0 to lenth of the entered password
    if(len(inputPassword) >= 8):                  #if the lenght of the password is greater than or equal to 8 
        if (inputPassword[charIndex] >= 'a' and inputPassword[charIndex] <= 'z' or inputPassword[charIndex] >= 'A' and inputPassword[charIndex] <= 'Z'):   #checking the alphabet
            alphabets+=1                 #adding 1 for each alphabet chars
        elif (inputPassword[charIndex] >='0' and inputPassword[charIndex] <= '9'):    #checking the numbers
            numbers+=1     #adding 1 for each number chars
        else:                 #the else part is for the special characters
            specialChar+=1       #adding 1 for each special characters
    else:
        print("Your password must be contain 8 or more characters")  #if the length of the password less than 8 it shows the message
        break
if(alphabets >= len(inputPassword) or numbers >= len(inputPassword) or specialChar >= len(inputPassword)):
    print("entered password is weak")        # if the user enter all the chars as alphabets or number or specila chars the password is weak   
elif(alphabets >=3 and numbers >=2 and specialChar >= 1):       #if the password contains 3 or more alphabets and two or more numbers and  one or more specialChar
    if(len(inputPassword) >= 16):             #if the password passes the above condition and len(inputPassword) >=16, the password is very strong
        print("entered password is is very strong")
    else:                                   #if the password passes the above condition and not len(inputPassword) >=16, the password is strong     
        print("entered password is strong")
elif((alphabets == 1 or numbers == 1 or specialChar == 1)):
    print("entered password is ok")    #if the password is not matches to above conditions password is ok

'''
outputs:-
Password: abcdefgh
entered password is weak

Password: abcdef!@#1
entered password is ok

Password: abcdefg!@#123
entered password is strong

Password: abcdefghij!@#$%12345678
entered password is is very strong

Password: asdf
Your password must be contain 8 or more characters
'''