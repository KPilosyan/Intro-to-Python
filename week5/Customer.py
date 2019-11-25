import Productcheck

def buy(product, num, price):
    if Productcheck.check(product, num) == True:
        print("You bought", product, "and spent", str(num*price))
    else:
        print("Sorry! We are out of this product")


buy("candy", 100, 100)