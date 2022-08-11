lunchPerPerson = int(input("Lunch per person: "))  #getting lunch cost per person as input
breakfastPerPerson = lunchPerPerson/2    #for breakfast per person is half of the lunch cost per person
hallPerPerson = lunchPerPerson*0.75      #for hall cost per person is one third of lunch cost per person
decorationPerPerson = hallPerPerson*0.50     #for decoration cost per person is half of hall cost per person
parkingPerPerson = hallPerPerson*0.10        #for parking cost per person is 10% of hall cost per person
totalCostPerPerson = lunchPerPerson+breakfastPerPerson+hallPerPerson+decorationPerPerson+parkingPerPerson    
#the total cost is sum of lunch, breakfast, hall, decoration and parking
numberOfPerson = int(input("Number of persons: "))  #getting number of person in input
totalCost = numberOfPerson*totalCostPerPerson       # the overall cost is number person get * total cost per person
brideCost = totalCost/2        # the overall cost is splited by two for groom and bride, so bride gets half of the overall cost 
loanAmount = brideCost - 50000     #if the half of the amount is exeeds the saving of bride that is 50000 they have to take a loan
if (brideCost > 50000):                #checking whether the bride have to take loan or not
    print("Yes they have to take loan")
    print("Loan amount is", round(loanAmount))     # if they have to take loan, printing tha loan amoumt
else:
    print("The total cost is", round(brideCost))
    print("They can save", round(50000-brideCost))
    print("No need of loan")    #if not printing that their is no need of loan
