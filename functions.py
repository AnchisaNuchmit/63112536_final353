
def buything(type, number):
    price = 0 
    if type == 1:
        print(type)
        print (number,"glasses")
        price = number*55
        print("price :",price)
        return(price)
    elif type == 2:
        print(type)
        print (number,"glasses")
        price = number*60
        print("price :",price)
        return(price)
    elif type == 3:
        print(type)
        print (number,"glasses")
        price = number*65
        print("price :",price)
        return(price)
    elif type == 4:
        print(type)
        print (number,"glasses")
        price = number*70
        print("price :",price)
        return(price)
    
def discountprice(total, number):   
        answer = input("Do you take glasses from home? True or False?")
        if answer == "True":
            print("Get discount 5 Baht each glasses.")
            discount = number*5
            total= total-discount
        elif type == "False":
            print("Do not get discount 5 Baht each glasses.")
        return (total)
       
    
