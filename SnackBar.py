"Write an app to calculate the total bill at the Snack bar." 
"The price of coffee is Rs 100, Vadai (1) is Rs100,"
"Sandwich is Rs 200,"
"Coke Rs 60."
"If the customer buys more than one sandwich or more than two vadai, the price of coffee is Rs 50." 
"If the customer buys one of each item, then there is discount of 20% of the total. No further discounts after the 20% discount."
"If the total price of the bill is more than Rs1000, then also there is a 20% discount." 

coffeePrice = 100
vadaiPrice = 100
sandwichPrice = 200
cokePrice = 60
totalAmount = 0
discountAmount = 0
isDiscounted = False

coffeeCount = int(input("Enter number of coffee: "))
vadaiCount = int(input("Enter number of vadai: "))
sandwichCount = int(input("Enter number of sandwich: "))
cokeCount = int(input("Enter number of coke: "))

totalAmount = ((coffeeCount * coffeePrice) + (vadaiCount * vadaiPrice) + (sandwichCount * sandwichPrice) + (cokeCount * cokePrice))  #total amount
print(totalAmount)
if(isDiscounted == False and sandwichCount > 1 or vadaiCount > 2):   #if the sandwich is greater than 1 and vadai is  greater than 2
    discountAmount = (coffeeCount * coffeePrice)*0.50              #discount is 50% of the coffee prize
    totalAmount = totalAmount - discountAmount                   #calculate the total amount
    print(discountAmount)
    isDiscounted = True
if(isDiscounted == False and coffeeCount >= 1 and vadaiCount >= 1 and sandwichCount >= 1 and cokeCount >= 1):       #coustomer buys everthing they get 20% off
    discountAmount = totalAmount*0.2
    totalAmount = totalAmount - discountAmount
    print(discountAmount)
    isDiscounted = True
if (isDiscounted == False and totalAmount > 1000):            #if the coustomer payment exceed to 1000rs they get 20% off
    discountAmount = totalAmount*0.2
    totalAmount = totalAmount - discountAmount
    print(discountAmount)
    isDiscounted = True
print("The Total amount is ",totalAmount)
