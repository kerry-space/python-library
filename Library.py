from Book import Book
from Magazine import Magazine
from LibraryUser import LibraryUser

class Library:
    def __init__(self):
        self.items  =[];
        self.users = [];

    def add_item(self,item):
        if item not in self.items:
            self.items.append(item)
            print(f"Added {item.title} to the library.")
        else:
            print(f"{item.title} already been add to library.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Removed {item.title} from the library.")
        else:
            print(f"{item.title} is been removed from library already.")


    def register_user(self,user):
        if user not in  self.users:
            self.users.append(user)
            print(f"{user} registered")
        else:
            print(f"{user} is already registered.")



    def borrow_item(self, user, item):
        if item in self.items and not item.is_borrowed:
            user.borrow(item)
            item.is_borrowed = True
            print(f"{user.name} borrowed {item.title}.")
        else:
            print(f"{item.title} is not available for borrowing.")

    
    def return_item(self, user, item):
        if item in user.borrowed_items:
            user.return_item(item)
            item.is_borrowed = False
            print(f"{user.name} returned {item.title}.")
        else:
            print(f"{user.name} has not borrowed {item.title}.")

    
    def list_borrowed_items(self):
        if self.borrowed_items:
            print(f"{self.name} has borrowed the following items:")
            for item in self.borrowed_items:
                item.display_info() 
        else:
            print(f"{self.name} has not borrowed any items.")