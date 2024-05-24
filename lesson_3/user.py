class User:
    def __init__(self, first_name, last_name):
        print("Hi!")
        self.firstName = first_name
        self.lastName = last_name
        
    def sayName(self):
        print("My name is", self.firstName)

    def sayLastName(self):
        print("My last name is", self.lastName)

    def sayFullName(self):
        print("I am", self.firstName, self.lastName, "^_^")