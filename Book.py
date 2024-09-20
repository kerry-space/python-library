from Item import Item 


class Book(Item):
    def __init__(self, title, author, year, pages):
        # Call the parent class's constructor
        super().__init__(title, author, year)
        self.pages = pages

    #overrid method
    def display_info(self):
        print(f"Book: {self.title}, Author: {self.author}, Year: {self.year}, Pages: {self.pages}")
               

