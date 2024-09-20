from Book import Book
from Magazine import Magazine
from Library import Library
from LibraryUser import LibraryUser

from Book import Book
from Magazine import Magazine
from Library import Library
from LibraryUser import LibraryUser

# Create library and users
library = Library()
user1 = LibraryUser("Alice")
book1 = Book("Python 101", "John Doe", 2021, 350)
magazine1 = Magazine("Tech Today", "Jane Smith", 2023, 45)

# Register user and add items
library.register_user(user1)
library.add_item(book1)
library.add_item(magazine1)

# Borrow and return items
library.borrow_item(user1, book1)
library.return_item(user1, book1)