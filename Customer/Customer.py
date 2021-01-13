import os
import json
import datetime
from   datetime  import datetime,date
from   BookStore import Book


class Customer(Book.Book.Book):
    purchase_quantity = 0
    invoices = {}
    invoices['context'] = []

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
        self.invoices['context'].append(self.__dict__) 

        with open('invoices.txt', 'a') as outfile:
            json.dump(self.invoices, outfile)
        outfile.close

        os.system('touch '+ self.name + '.txt')
        with open(self.name +'.txt' , 'w') as outfile:
            json.dump(self.__dict__, outfile)
        outfile.close
        print("Invoice exported successfully.")
        self.purchase_quantity += 1

    def time_interval(self):
        counter = 0
        first_interval_year = input("Please enter first time interval's year : ")
        first_interval_month = input("Please enter first time interval's month : ")
        first_interval_day = input("Please enter first time interval's day : ")
        first_interval_date = datetime.date(first_interval_year,first_interval_month,first_interval_day)
        print("First interval date is :",first_interval_date.strftime("%B %d, %Y"))
        
        second_interval_year = input("Please enter second time interval's year : ")
        second_interval_month = input("Please enter second time interval's month : ")
        second_interval_day = input("Please enter second time interval's day : ")
        second_interval_date = datetime.date(second_interval_year,second_interval_month,second_interval_day)
        print("Second interval's date is :",second_interval_date.strftime("%B %d, %Y"))

        with open('invoices.txt') as json_file:
            invoices_dict = json.load(json_file)
            for temp_invoice in invoices_dict['context']:
                purchase_date = datetime.strptime(temp_invoice['purchase_date'],"%B %d, %Y")
                if first_interval_date < purchase_date < second_interval_date :
                    counter += 1

                    