from BookStore import Book

class Customer():
    def __init__(self,name,last_name,purchase_date,book_choice):
        self.name = name
        self.last_name = last_name
        self.purchase_date = purchase_date
        self.book_choice = book_choice
        pass
    