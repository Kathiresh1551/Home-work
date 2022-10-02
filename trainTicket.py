'''
Calculate the cost of train tickets. Single one way ticket from Madurai to Chennai (or vice versa) is Rs1000. 
Adding a return ticket will cost Rs750 extra.
Family of 4 or more gets 20% off. Senior rate is 50% off. 
'''

print("welcome to KB Travels")
print("Bus for Madurai to Chennai")
travelCost = 1000
seniorCitizenCost = 500
returnCost = 750
seniorReturnCost = 750/2
totalCost = 0

def returnFunction(totalCost, membersCount, isSenior):
    if(isSenior == 0):
        totalCost += (membersCount*returnCost)
    else:
        totalCost += ((membersCount-isSenior)*returnCost)
        totalCost += isSenior*seniorReturnCost
    return totalCost


def costCalculation(membersCount, isSenior):
    if(membersCount >= 4 and isSenior == 0):
        totalCost = (membersCount*travelCost)
        totalCost -= totalCost*0.2
    elif(membersCount >= 4 and isSenior >= 1):
        totalCost = ((membersCount-isSenior)*travelCost)
        totalCost += isSenior*seniorCitizenCost
        totalCost -= totalCost*0.2
    elif(membersCount == isSenior):
        totalCost = isSenior * seniorCitizenCost
    else:
        totalCost = (membersCount*travelCost)
    return round(totalCost)

isReturn = input("Return?(type yes or no): ")
membersCount = int(input("How many members?:" ))
isSenior = int(input("Senior Citizen: "))

nonReturnCost = costCalculation(membersCount, isSenior)

if(isReturn == "yes"):
    returnCost = returnFunction(nonReturnCost,  membersCount, isSenior)
    print(round(returnCost))
else:
    print(round(nonReturnCost))

'''
welcome to KB Travels
Bus for Madurai to Chennai
Return?(type yes or no): no
How many members?:1
Senior Citizen: 0
1000


welcome to KB Travels
Bus for Madurai to Chennai
Return?(type yes or no): yes
How many members?:1
Senior Citizen: 0
1750

welcome to KB Travels
Bus for Madurai to Chennai
Return?(type yes or no): yes
How many members?:2
Senior Citizen: 2
1750

welcome to KB Travels
Bus for Madurai to Chennai
Return?(type yes or no): no
How many members?:4
Senior Citizen: 0
3200

welcome to KB Travels
Bus for Madurai to Chennai
Return?(type yes or no): no
How many members?:4
Senior C
'''