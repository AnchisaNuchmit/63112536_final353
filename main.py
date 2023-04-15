from functions import buything, discountprice

total = int()
buying = str("y")
while buying == "y" :
    type = int(input("Plase select (1) Espresso (2) Cappuccino (3) Latte (4) Mocha : "))
    if type >= 5 or type <= 0 :
        print("Wrong Selection. Plase select on the list only.")
       
    
    else :
        number = int(input("Plase input number of glasses : "))
        total = buything(type, number)
        realtotal = discountprice(total, number)   
    
        print("Total price :",realtotal)
    buying = str(input("Do you want to make another order? y/n : "))

print("Thank you :)")





