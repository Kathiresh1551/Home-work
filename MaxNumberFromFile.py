file1 = open("C:\\Users\itssm\python\Sayur\Home-work\Others\\CafeItemDetails.csv","r")
arrList = file1.readlines()
itemList = []
priceList = []

for index in range (0, len(arrList)):
    arrListSpilt = arrList[index]
    newlist = arrListSpilt.split(",")
    itemList.append(newlist[0])
    priceList.append(newlist[1])
    

priceList.pop(0)
Costlyrate = max(priceList, key=int)
CostlyItem = priceList.index(Costlyrate)
print("The costliest dish is", itemList[CostlyItem+1],"with ₹",Costlyrate)


'''
in file1

Item	Prize
Vadai	8
Coke	20
Burger	80
Coffee	10
Pizza	100


output
The costliest dish is Pizza with ₹ 100
'''
