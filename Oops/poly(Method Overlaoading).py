class info():
    def display(self):
        print("This is a normal display")

    def display(self, Name=None):
        print(f"This is second display {Name}")

o = info()
o.display()