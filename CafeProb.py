# Write an app for the cafe. Calculate the sales for the day. 
# Use a function to calculate each customer sale. Also, Use the function to restock the supply of items if the supply 
# goes down to 20% of the original supply. Print how many times the supply was restocked. 
# Also print the total numbers of items sold.
# (Previous HW had the instructions for running a cafe. You can use that as a starting point)

vadaiSupply = 100
soldVadai = 0
vadaiCost = 10
restockCount = 0
totalAmount = 0
minimumOrinalSupply = vadaiSupply * 0.2


def restockFuntion (restockCount):
    restockCount += 1
    currentSupply = vadaiSupply
    return [restockCount, currentSupply]
    

def saleCalculation (totalAmount, vadaiSupply, restockCount, soldVadai):
    for index in range(0, 5):
        print("customer", index + 1)
        reqVadai = int(input("vadai: "))
        soldVadai += reqVadai
        totalAmount += reqVadai * 10
        vadaiSupply -= reqVadai
        if(vadaiSupply <= minimumOrinalSupply):
            detailsList = restockFuntion(restockCount)
            restockCount = detailsList[0]
            vadaiSupply = detailsList[1]
    

    print('totalAmount', totalAmount)
    print('restockCount', restockCount)
    print('soldVadai', soldVadai)
    # return totalAmount, soldVadai, restockCount0


saleCalculation(totalAmount, vadaiSupply, restockCount, soldVadai)


'''
input: 
    customer 1
    vadai: 80
    customer 2
    vadai: 90
    customer 3
    vadai: 40
    customer 4
    vadai: 50
    customer 5
    vadai: 20
output:
    totalAmount 2800
    restockCount 3
    soldVadai 280


input: 
    customer 1
    vadai: 10
    customer 2
    vadai: 6
    customer 3
    vadai: 9
    customer 4
    vadai: 5 
    customer 5
    vadai: 8

output: 
    totalAmount 380
    restockCount 0
    soldVadai 38

'''