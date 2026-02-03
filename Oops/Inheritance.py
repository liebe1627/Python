class Animal:
    def __init__(self,Type):
        self.Type = Type
    def Dog(self):
        print("There is a Dog",self.Type)
        self.Name = "Bruno"

class AnimalKingdom(Animal):
    def __init__(self, Type, Name):
        super().__init__(Type)
        self.Name = Name

    def Dog(self):
        super().Dog()
        print("Type of the dog is: ",self.Type,self.Name)

Obj = AnimalKingdom("Some","Name")
Obj.Dog()