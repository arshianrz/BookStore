from BookStore import Book
from datetime import date
import json

class Customer(Book.Book.Book):
    def __init__(self,name,last_name,purchase_date,book_choice):
        self.name = name
        self.last_name = last_name
        self.purchase_date = purchase_date
        self.book_choice = book_choice
        self.today = date.today()

    def purchase(self):
        self.book_choice = str(input("You are going to purchase a book , Please write down book's name : \n"))
        with open('Books.txt') as json_file:
            book_dict = json.load(json_file)
            for temp_book in book_dict['context']:
                if self.book_choice != temp_book['name']:
                    print("Book not found.")
                elif self.book_choice == temp_book['name']:
                    quantity = int(temp_book['quantity'])
                    if quantity-1 == 0 :
                        self.remove_book()
                    else :
                        temp_book['quantity'] = str(quantity - 1)

    def invoice(self):
        self.name = input("Customer name : ")
        self.last_name = input("Customer Last Name : ")
        self.purchase_date = self.today.strftime("%B %d, %Y")
        invoice = { "name":self.name,
                    "last_name":self.last_name,
                    "Book":self.book_choice,
                    "purchase_date":self.purchase_date}
                    
        with open('invoice.txt', 'a') as outfile:
            json.dump(invoice, outfile)
        outfile.close
        print("Invoice exported successfully.")