"Write an app for a phone sales man."
"The Salesman earns Rs10000 every month."
"He earns Rs1000 commission for every phone he sells." 
"If he sells more than 5 phones a month, he extra Rs100 per phone (1000+100)."
"If he sells 10 phones or more, he gets extra Rs 200 for each phone over 5."
"He can only earn max 25000 per month. Calculate his monthly salary and avg salary per month in one year. "

salesManFixedSalary = 10000
commission = 1000
maxSalary = 25000
salaryPerMonth = 0
salaryPerYear = 0
avgSalary = 0
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

for perMonth in range (0, len(month)):     #for loop in range of 0 to 12
    phoneSold = int(input("Number of phone sold in " + month[perMonth] + ": " ))   #getting input as phoneSold
    if (phoneSold > 0):                            #if PhoneSold is greater than 0, the salesman fixed salary plus phone sold * 1000
        salaryPerMonth = salesManFixedSalary + phoneSold * 1000
    else:
        salaryPerMonth = salesManFixedSalary   #if the salesman doesn't sale any phone he gets the fixed salary
        
    if (phoneSold > 5 and phoneSold < 10):    #if the phone sold is in between of 5 to 10 the bonus amount is 1000 + 100
        salaryPerMonth = salesManFixedSalary + (phoneSold * 1000) + ((phoneSold - 5) * 100)
    elif (phoneSold >= 10):           #if the phone sold is more than 10 the bonus amount is 1000 + 200
            salaryPerMonth = salesManFixedSalary + (phoneSold * 1000) + ((phoneSold - 9) * 200)

    if (salaryPerMonth > 25000):            #the sales man salary doesn't exeeds to 25000
        salaryPerMonth = 25000  
    
    salaryPerYear += salaryPerMonth          #adding all the phonesold count permonth

print(salaryPerYear)
avgSalary = salaryPerYear / len(month)
print("The average salary per year is: ", round(avgSalary))      #the final output is the average salary per year that is 120000 / 12 = 10000
