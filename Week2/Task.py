# ---------------------------------------------------------------------
# N1
# class People:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
        
#     def getmail (self):
#         return f"{self.firstname}.{self.lastname}.uni@btu.edu.ge"
    
# class Lecturer(People):
#     def __init__(self, firstname, lastname, salary):
#         self.salary = salary
#         super().__init__(firstname, lastname)
        
#     def getmail (self):
#         return f"{self.firstname}.{self.lastname}@btu.edu.ge"
    
# class Student(People):
#     def __init__(self, firstname, lastname, courses):
#         self.coruses = courses
#         super().__init__(firstname, lastname)
        
#     def getmail (self):
#         return f"{self.firstname}.{self.lastname}.1@btu.edu.ge"
    
# p1 = Student("nika", "gamkrelidze", 10)
# print(p1.getmail())

# ---------------------------------------------------------------------
# N2

# class LibraryItem:
#     def __init__(self, status, title=None, subject=None ):
#         if title is not None: self.title = title
#         if title is not None: self.subject = subject
#         self.status = status
    
#     def booking(self):
#         pass

# class Book(LibraryItem):
#     def __init__(self, status, title, subject,  ISBN, authors):
#         self.ISBN = ISBN
#         self.authors = authors
#         super().__init__(title, subject, status)
        
# class Magazine(LibraryItem):
#     def __init__(self, status, ISBN, authors):
#         self.ISBN = ISBN
#         self.authors = authors
#         super().__init__(status)
        
# class CD(LibraryItem):
#     def __init__(self, status, title):
#         super().__init__(status, title)
        
#     def booking(self):
#         return "Error"
        
# ---------------------------------------------------------------------
# N3

# class Contacts:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
# class MailSender:
#     def sendMail(self):
#         return "Mail sended"
        

# class Friend(Contacts, MailSender):
#     def __init__(self, name, phone, email):
#         self.email = email
#         super().__init__(name, phone)

# class Family(Contacts, MailSender):
#     def __init__(self, name, phone, email, birthday):
#         self.birthday = birthday
#         self.email = email
#         super().__init__(name, phone)

        
# Fam1 = Friend("nika",555,"@gmail")
# print(Fam1.sendMail())

# ---------------------------------------------------------------------
# N4

# class People:
#     def __init__(self, firstname=None, lastname=None):
#         if firstname is not None: self.firstname = firstname
#         if lastname is not None: self.lastname = lastname

#     def getmail (self):
#         return f"{self.firstname}.{self.lastname}.uni@btu.edu.ge"

# class Lecturer(People):
#     def __init__(self, firstname=None, lastname=None, salary=None):
#         if salary is not None : self.salary = salary
#         super().__init__(firstname, lastname)

#     def getmail (self):
#         return f"{self.firstname}.{self.lastname}@btu.edu.ge"

# class Student(People):
#     def __init__(self, firstname=None, lastname=None, courses=None):
#         if courses is not None: self.coruses = courses
#         super().__init__(firstname, lastname)

#     def getmail (self):
#         return f"{self.firstname}.{self.lastname}.1@btu.edu.ge"

# class DoctoralStudent(Student, Lecturer):
#     def __init__(self, firstname=None, lastname=None, courses=None, salary=None):
#         super().__init__(firstname, lastname, courses)
#         Lecturer.__init__(self, salary=salary)
    
#     def getmail(self):
#         return f"{self.firstname}.{self.lastname}.D.student@btu.edu.ge"


# p1 = DoctoralStudent("Nika", "Gamkrelidze", 5, 50000)
# print(p1.getmail())