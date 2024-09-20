from Item import Item 


class Magazine(Item):
    def __init__(self, title, author, year, issue) -> None:
        super().__init__(title, author, year)
        self.issue = issue

    def display_info(self):
        #overrid it
        print(f"Magazine: {self.title}, Author: {self.author}, Year: {self.year}, Issue: {self.issue}")
      