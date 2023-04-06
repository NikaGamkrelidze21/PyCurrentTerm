class Ticket:
    def __init__(self, movie, price, amount, language="Geo"):
        self.movie = movie
        self.price = price
        self.amount = amount
        self.language = language
        print("+ "*20 + "\nCREATED " + self.__str__() + "\n"+"+ "*20)

    def __str__(self):
        return f"""Movie: {self.movie} \nPrice: {self.price} \nAmount: {self.amount} \nLanguage: {self.language}"""
    
    def __lt__(self, other):
        if isinstance(other, Ticket):
            return self.amount < other.amount
        elif isinstance(other, int):
            return self.amount < other
        
    def __le__(self, other):
        if isinstance(other, Ticket):
            return self.amount <= other.amount
        elif isinstance(other, int):
            return self.amount <= other
        
    def __gt__(self, other):
        if isinstance(other, Ticket):
            return self.amount > other.amount
        elif isinstance(other, int):
            return self.amount > other
        
    def __ge__(self, other):
        if isinstance(other, Ticket):
            return self.amount >= other.amount
        elif isinstance(other, int):
            return self.amount >= other
        
    def __eq__(self, other):
        if isinstance(other, Ticket):
            return self.amount == other.amount
        elif isinstance(other, int):
            return self.amount == other
        
    def __ne__(self, other):
        if isinstance(other, Ticket):
            return self.amount != other.amount
        elif isinstance(other, int):
            return self.amount != other
         

class User:
    def __init__(self, name, balance):
        self.balance = balance
        self.name = name
        print("+ "*20 + "\nCREATED " + self.__str__() + "\n"+"+ "*20)

    def __str__(self):
        return f"""\nName: {self.name} \nBalance: {self.balance}"""
    
    def  deposit(self, money):
        self.balance += money
        
    def buy_ticket(self, ticket, amount):
        ballance_ok = True if self.balance >= amount * ticket.price else "Ballance is not enough"
        tickets_ok = True if ticket.amount >= amount else "Tickets are not enough"
        
        def allow() : return  ballance_ok == True and tickets_ok==True 
        
        def execute() : 
            self.balance -= amount * ticket.price
            ticket.amount -= amount
            print("\nAccepted "+"- "*20 + f"\nyou purchased {amount} tickets")
            print(" -"*24)


        if allow():
            execute()
        else:
            print("\nDeclined "+"- "*20)
            print("YOU CAN NOT PURCHASE TICKETS BECAUSE:")
            for i in (ballance_ok, tickets_ok):
                print() if i == True else print(i)   
            print(" -"*24)
            
t1 = Ticket("Avatar", 10, 10)

u1 = User("Nika", 200)
u2 = User("Nika", 10)


u1.buy_ticket(t1, 1)
u1.buy_ticket(t1, 200)
u2.buy_ticket(t1, 5)
u1.buy_ticket(t1, 10)


print("\n")
print(t1)
print("\n")
print(u1)
print(u2)
print("\n")
print(t1 > t1)
print(t1 > 15)

