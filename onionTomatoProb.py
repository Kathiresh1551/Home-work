Tomato = 10.5 #declaring Tomato price
city = str(input("City: ")) #geting city from user
budget = int(input("Budget: ")) #geting budget from user

if(city == "chennai"): #city equal to chennai the onion price gonna be 30rs
    Onion = 30
elif(city == "madurai"): #city equal to madurai the onion price gonna be 30rs
    Onion = 34
elif(city == "coimbatore"): #city equal to coimbatore the onion price gonna be 30rs
    Onion = 27
else: #if city is not equals to all others, its gonna be 20rs
    Onion = 20

petrol = budget*0.03 #for petrol we take 3% from the budget
balanceAmount = budget - petrol #balance amount
tomatoPerKg = balanceAmount//Tomato #in the balance amount we can buy this amount on tomato
onionPerKg = balanceAmount//Onion #in the balance amount we can buy this amount on onion
print ("petrol", petrol)
print ("Tomato: ", tomatoPerKg,"kg" )
print ("Onion: ", onionPerKg,"kg")

