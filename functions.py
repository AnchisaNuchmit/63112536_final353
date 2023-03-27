
def buything():
    price = 0
    type = int(input("Plase select (1) Espresso (2) Cappuccino (3) Latte (4) Mocha : "))
    if type > 4 or type < 0 :
        print("Wrong Selection. Plase select on the list only.")
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
       
    def discountprice(price):   
        answer = input("Do you take glasses from home? True or False?")
        if answer == "True":
            print("Get discount 5 Baht each glasses.")
            discount = number*5
            price = price-discount
        elif type == "False":
            print("Do not get discount 5 Baht each glasses.")
        return (price)