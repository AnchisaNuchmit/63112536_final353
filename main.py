from functions import buything, discountprice

total = 0
number = 0
buying = str("y")
while buying == "y" :
    total = buything()
    totalprice = discountprice()
    print("Total price :",total)
    buying = str(input("Do you want to make another order? y/n : "))

print("Thank you :)")



