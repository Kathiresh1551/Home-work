subjectCount = 5
passCount = 0
notValid = 0
nintyAbove = 0
fourtyAbove = 0
seventyFiveAbove = 0
fiftyAbove = 0

for n in range(1,subjectCount+1):
    print ("Subject", n)
    marks = int(input("Enter your mark: "))

    if (marks > 40 and marks <= 100):                                            #if marks greater than 40 and less than 100
        if (marks >= 90 and marks <= 100):                                       #if marks greater than 90 and less than 100
            nintyAbove+=1                                                        #increasing nintyAbove 1 by 1
        elif (marks >= 75 and marks <= 90 or marks >= 75 and marks <= 100):      #if marks greater than 75 and less than less than 90 or less than 100
            seventyFiveAbove+=1                                                  #increasing seventyFiveAbove 1 by 1
        elif (marks >= 50 and marks <= 75):                                      #if marks greater than 50 and less than 75
            fiftyAbove += 1                                                      #increasing fiftyAbove 1 by 1
        elif (marks >= 40 and marks <= 50):                                      #if marks greater than 40 and less than 50
            fourtyAbove+=1                                                       #increasing fourtyAbove 1 by 1
        elif (marks >= 60 and marks <= 100):                                     #if marks greater than 60 and less than 100
            passCount+=1                                                         #increasing passCount 1 by 1
    elif(marks > 100):                                                           #if marks greater than 100
        notValid+=1                                                              #increasing notValid 1 by 1
        break                              

if(nintyAbove <= 3 and fourtyAbove <= 2 or seventyFiveAbove <= 3 and fiftyAbove <= 2 or passCount == 5):
    print ("Result is Pass")          #if the condition is true printing the result as Result is pass
elif(notValid > 0):                   #if the condition is true printing the result as enter a valid number
    print ("enter a valid number")
else:                                 #if all the condition fails printing the result as Result is Result is Fail
    print("Result is Fail")
