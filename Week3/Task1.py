class Cat:
    def eat(self):
        print("Cat eats a milk")
    def talk(self):
        print("Cat says miaww")
    def walk(self):
        print("Cat can run 20km/h")
        
class Dog:
    def eat(self):
        print("Dog eats a bone")
    def talk(self):
        print("Dog says Aww")
    def walk(self):
        print("Dog can run 40km/h")
        
d1 = Dog()
c1 = Cat()

for i in (d1, c1):
    i.eat()
    i.walk()
    i.talk()
