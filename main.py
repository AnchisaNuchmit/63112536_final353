
price = 0
total = 0
number = 0
buying = str("y")
while buying == "y" :
    def buything(price):
        type = int(input("Plase select (1) Espresso (2) Cappuccino (3) Latte (4) Mocha : "))
        if type > 4 or type < 0 :
            print("Wrong Selection. Plase select on the list only.")
            buying = str(input("Do you want to make another order? y/n : "))
            type = int(input("Plase select (1) Espresso (2) Cappuccino (3) Latte (4) Mocha : "))

        number = int(input("Plase input number of glasses : "))
        if type == 1:
            print(type)
            print (number,"glasses")
            price = number*55
            print("price :",price)
            return("Espresso")
        elif type == 2:
            print(type)
            print (number,"glasses")
            price = number*60
            print("price :",price)
            return("Cappuccino")
        elif type == 3:
            print(type)
            print (number,"glasses")
            price = number*65
            print("price :",price)
            return("Latte")
        elif type == 4:
            print(type)
            print (number,"glasses")
            price = number*70
            print("price :",price)
            return("Mocha")
        
        answer = input("Do you take glasses from home? True or False?")
        if answer == "True":
            print("Get discount 5 Baht each glasses.")
            discount = number*5
            price = price-discount
        elif type == "False":
            print("Do not get discount 5 Baht each glasses.")
        return (price)

    total = buything(price)
    print("Total price :",total)
    buying = str(input("Do you want to make another order? y/n : "))

print("Thank you :)")



