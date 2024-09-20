class Item:
    
    # Constructor: initializes the attributes, 
    # self ==  refers to the instance of the class itself
    def __init__(self, title, author, year ) -> None:
        self.title  = title
        self.author = author
        self.year = year
        self.is_borrowed = False
    
    # Define a method (function) inside the class
    def display_info(self):
        raise NotImplementedError("Subclasses should implement this!")

