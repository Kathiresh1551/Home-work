# Check if the username and password is correct. 
# Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end.
# passward is the first, third, and last 3 letters of the username followed by the first three letters of the 
# name of the company mentioned in the username, followed by any 3 numbers.
# eg username : myname@sayur.com. password - mnamesay123S

inputUsername = input("enter username: ")           #username input
inputPassword = input("enter password: ")           #password input
userNameValidation1 = inputUsername[-4:]            #usernameValidation for .com and .edu
userNameValidation2 = inputUsername[-5:]            #usernameValidation for .tech
userNameValidation3 = inputUsername[-3:]            #usernameValidation for org
passwordSplit = ""                                  
atChar = 0
noatChar = 0
invalidUsername = 0
validPassword = 0
incorrectPassword = 0

passwordSplit = inputPassword.split('[^0-9]+')       #spliting the password by alphabets and numbers

for index in range (len(inputUsername)):
    if(inputUsername[index] == '@'):
        atChar += 1
    else:
        noatChar += 1
if(noatChar == len(inputUsername)):
    print("invalid user name")
else:
    companyName = inputUsername.split('@')              #getting the company name
    companySubName = companySubName = companyName[1][0:3]                #getting the sub name of the companyName the is 1st three chars

for passwordChar in range (len(inputPassword)):
    if(inputPassword[passwordChar] >= '0' and inputPassword[passwordChar] <= '9'):
        a = inputPassword.split(inputPassword[passwordChar])
        passwordSplit=a[0]     #getting the 1st 3 letters of the companyName in password
        break 


for index in range (0, len(inputUsername)):
    if(noatChar != len(inputUsername)):
        atChar += 1
        if(len(inputUsername) > 4 and userNameValidation1 == ".com" or userNameValidation1 == ".edu"):        #checking the end chars of the username
            if(inputUsername[0] == inputPassword[0] and inputUsername[2] == inputPassword[1] and passwordSplit[-3:] == companySubName):
                validPassword += 1
            else:                                 
                incorrectPassword += 1
        elif(len(inputUsername) > 5 and userNameValidation2 == ".tech"):                            #checking the end chars of the username
            if(inputUsername[0] == inputPassword[0] and inputUsername[2] == inputPassword[1] and passwordSplit[-3:] == companySubName):
                validPassword += 1
            else:                                 
                incorrectPassword += 1
        elif(len(inputUsername) > 4 and userNameValidation3 == "org"):              #checking the end chars of the username
            if(inputUsername[0] == inputPassword[0] and inputUsername[2] == inputPassword[1] and passwordSplit[-3:] == companySubName):
                validPassword += 1
            else:                                 
                incorrectPassword += 1
        else:
            print("inncorrect password")
            break
if(validPassword == len(inputUsername)):
    print("password successfull")
elif(noatChar != len(inputUsername)):                           
    print("password not success")

'''
output:

enter username: kathir@amphi.com
enter password: ktamp000
password successfull

enter username: kathiresh        
enter password: kathiresh
invalid user name

enter username: .com      
enter password: .com
invalid user name

enter username: myname@sayur.com 
enter password: mnamesay123S     
password successfull

'''