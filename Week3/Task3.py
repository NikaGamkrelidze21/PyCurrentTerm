class Person:
    def __init__(self, name, deposit=100, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan
    def  __str__(self):
        return f"name: {self.name} \ndeposit: {self.deposit} \nloan: {self.loan}"
        
class House:
    def __init__(self, ID, price, owner, status):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = status
        
    def sell(self, buyer, loan=None):
        if loan is None:
            self.owner.deposit += self.price
            buyer.deposit -= self.price
            self.status = "sold"
            print(f"{self.owner.name} sold - House (ID:{self.ID}) to {buyer.name}")
            self.owner = buyer
            
        else:
            self.owner.deposit += self.price
            buyer.deposit -= (self.price - loan)
            buyer.loan += loan
            self.status = "sold with debt"
            print(f"{self.owner.name} sold - House (ID:{self.ID}) to {buyer.name}")
            self.owner = buyer
            
        
p1 = Person("Nika")
p2 = Person("Nika2")
h1 = House(1,500,p1,"on sale")
h1.sell(p2, 250)
print(p1)
print(p2)
print(h1)