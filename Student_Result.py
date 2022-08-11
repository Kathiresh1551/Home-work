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

    if (marks > 40 and marks <= 100):
        if (marks >= 90 and marks <= 100):
            nintyAbove+=1
        elif (marks >= 75 and marks <= 90 or marks >= 75 and marks <= 100):
            seventyFiveAbove+=1
        elif (marks >= 50 and marks <= 75):
            fiftyAbove += 1
        elif (marks >= 40 and marks <= 50):
            fourtyAbove+=1
        elif (marks >= 60 and marks <= 100):
            passCount+=1
    elif(marks > 100):
        notValid+=1
        break

if(nintyAbove <= 3 and fourtyAbove <= 2 or seventyFiveAbove <= 3 and fiftyAbove <= 2 or passCount == 5):
    print ("Result is pass")
elif(notValid > 0):
    print ("enter a valid number")
else:
    print("Result is Fail")