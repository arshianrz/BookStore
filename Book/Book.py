import json

class Book:
    """
        [we should be able to create and delete book objects for our library.]
    """
    ID_counter = 1
    books_quantity = 0
    books = {}
    books['context'] = []

    def __init__(self, name, author, genre, price, quantity, ID):
        """
        [constructor]

        Args:
            name ([string]): [book title]
            author ([string]): [writer of the book]
            genre ([string]): [book's genre]
            quantity ([integer]): [number of specific book]
            price ([integer]): [book's price]
        """
        self.name = name
        self.author = author
        self.genre = genre
        self.quantity = quantity
        self.price = price
        self.ID = 1000 + Book.ID_counter
        Book.ID_counter += 1
        Book.books_quantity += self.quantity

    def book_info(self):
        """
        Prints a general information about a specific book.
        """
        print("ID : ",                      self.ID,
              "\nName : ",                  self.name,
              "\nAuthor : ",                self.author,
              "\nGenre : ",                 self.genre,
              "\nPrice : ",                 self.price,
              "\nQuantity of this book : ", self.quantity)

    def create_book(self):
        print("You are about to create a book ,please answer following questions.")
        self.name = input("Enter title :")
        self.author = input("Enter author :")
        self.genre = input("Enter genre :")
        self.price = input("Enter price :")
        self.quantity = input("Enter quantity :")
        self.ID = 1000 + self.ID_counter
        self.books['context'].append(self.__dict__)
        with open('Books.txt', 'a') as outfile:
            json.dump(Book.books, outfile)
        outfile.close
        print("Book named : ",self.name ,"\ncreated successfully with ID : ",self.ID)
        

    def remove_book(self):
        check = str(input("You are about to remove a book. \n Are you sure (Y/N) ?")).lower().strip()
        try:
            if check[0] == 'y':
                with open('Books.txt') as json_file:
                    book_dict = json.load(json_file)
                    for temp_book in book_dict['context']:
                        if self.name != temp_book['name']:
                            print("Book not found.")
                        elif self.name == temp_book['name']:
                            book_dict['context'].remove(temp_book)
                            with open('Books.txt', 'w') as outfile:
                                json.dump(Book.books, outfile)
                            outfile.close
                del self
                print("Book deleted successfully.")
            elif check[0] == 'n':
                print("Removing operation cancelled.")
                return False
            else:
                print('Invalid Input')
                return self.remove_book()
        except Exception as error:
            print("Please enter valid inputs")
            print(error)
            return self.remove_book()

    def search_book(self):
        check = str(input("Search by ID or Name ? \n (1 -> ID , 2 -> Name)")).lower().strip()
        try:
            if check[0] == '1' :
                with open('Books.txt') as json_file:
                    book_dict = json.load(json_file)
                    for temp_book in book_dict['context']:
                        if self.ID != temp_book['ID']:
                            print("Book with given ID not found.")
                        elif self.name == temp_book['name']:
                            self.book_info()
            elif check[0] == '2' :
                with open('Books.txt') as json_file:
                    book_dict = json.load(json_file)
                    for temp_book in book_dict['context']:
                        if self.ID != temp_book['Name']:
                            print("Book with given Name not found.")
                        elif self.name == temp_book['name']:
                            self.book_info()
            else:
                print('Invalid Input')
                return self.search_book()
        except Exception as error:
            print("Please enter valid inputs(1/2)")
            print(error)
            return self.search_book()