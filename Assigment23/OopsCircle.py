class Circle:

    Pi = 3.14

    def __init__(self):
        self.Radius = 0
        self.Area = 0
        self.Circumference = 0

    def Accept(self):
        self.Radius = int(input("Enter the radius: "))
    
    def CalculateArea(self):
        
        self.Area = Circle.Pi*self.Radius**2
    
    def CalculateCircumference(self):
        self.Circumference = 2*Circle.Pi*self.Radius
    
    def Display(self):
        print("Radius of the circle: ",self.Radius)
        print("Area of circle: ",self.Area)
        print("Circumference of circle: ",self.Circumference)

obj1 = Circle()
obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()

