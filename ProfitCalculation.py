cakeCostPrice = 20
cakeSellingPrice = 40
breadCostPrice = 10
breadSellingPrice = 15
employeeCount = 2
employeeSalary = 100
totalSalary = employeeCount * employeeSalary
customerCount = 10
totalProfit = 0

cakeProfit = cakeSellingPrice - cakeCostPrice #profit for cake  20
breadProfit = breadSellingPrice - breadCostPrice #profit for bread  5

for n in range(1, customerCount+1):  #for loop for coustomers
    print ("Coustomer: ", n)
    cakeCount = int(input("Enter Number of Cakes: "))  #get input as cake count
    breadCount = int(input("Enter Number of Breads: "))  #get input as bread count

    customerCakeProfit = cakeCount * cakeProfit  #Ex:- cakeCount is 4 cakeProfit is 20 so 10 * 20 = 200
    customerBreadProfit = breadCount * breadProfit #Ex:- breadCount is 4 breadProfit is 5 so 10 * 5 = 50
    totalProfit = totalProfit + cakeCount*cakeSellingPrice + breadCount*breadSellingPrice  #sum of totalProfit, cakeCount, breadCount

totalProfit = totalProfit - totalSalary   #for labours salary 

print("profit is ", totalProfit)   #the total salary
