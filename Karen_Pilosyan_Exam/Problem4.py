class Cafe:
    def __init__(self,name,tables):
        self.name = name 
        self.tables = tables
        self.menu =  {"salad": "10$", "pizza": "20$", "ice_cream": "5$", "cake": "15$"}

    def Reserve_tables(self):
        if self.tables > 0:
            self.tables-=1
            print("The reservation was made")
            print(str(self.tables),"tables left free")
        elif self.tables == 0:
            print("No available tables")

    def Checkout(self,food):
        for i in self.menu.keys():
            if i == food:
                print("You have ordered", food + ". You have a", self.menu[i], "dollar check.")
                break

    def Order(self,food):
        if food not in self.menu.keys():
            print("We are out of", food)
        else:
            self.Checkout(food)  
    
order1 = Cafe("Wendy's", 10)
order2 = Cafe("Artashnoc", 40)

order1.Reserve_tables()
order2.Order("cake")
order2.Order("chka")
