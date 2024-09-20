class LibraryUser:
    def __init__(self, name: str) -> None:
        self.name = name
        self.borrowed_items = []  
    
    def borrow(self, item):
        if item not in self.borrowed_items:
            self.borrowed_items.append(item)
            print(f"{self.name} borrowed {item.title}.")
        else:
            print(f"{item.title} is already borrowed by {self.name}.")


    def return_item(self, item):
        if item in self.borrowed_items:
            self.borrowed_items.remove(item)
            print(f"{self.name} returned {item.title}.")
        else:
            print(f"{self.name} cannot return {item.title} as it was not borrowed.")
    
    
    def list_borrowed_items(self):
        if self.borrowed_items:
            print(f"{self.name} has borrowed the following items:")
            for item in self.borrowed_items:
                item.display_info() 
        else:
            print(f"{self.name} has not borrowed any items.")
