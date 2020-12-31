import json

class Book:
    """
        [we should be able to create and delete book objects for our library.]
    """
    ID_counter = 1
    books_quantity = 0

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
        self.ID = ID
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
        serialized_object = json.dumps(self.__dict__)
        book_file = open("Books.txt", "a")
        book_file.write(serialized_object)
        book_file.close()

    def remove_book(self):
        check = str(input("You are about to remove a book. \n Are you sure (Y/N) ?")).lower().strip()
        try:
            if check[0] == 'y':
                del self
                print("Book deleted successfully.")
            elif check[0] == 'n':
                print("Removing operation cancelled.")
                return False
            else:
                print('Invalid Input')
                return self.remove_book(self)
        except Exception as error:
            print("Please enter valid inputs")
            print(error)
            return self.remove_book(self)