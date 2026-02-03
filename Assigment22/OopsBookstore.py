class bookstore:

    NoOfBook = 0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author

    def displayInfo(self):
        bookstore.NoOfBook +=1
        print(f"{self.Name} by {self.Author}. No of books: {bookstore.NoOfBook}")

obj1 = bookstore("Linux","Robert Love")
obj1.displayInfo()

obj2 = bookstore("Linux","Robert Love")
obj2.displayInfo()



    