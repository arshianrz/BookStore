class Book:
    """
        [we should be able to create and delete book objects for our library.]
    """
    books_quantity = 0
    def __init__(self,name,writer,genre,price,quantity):
        """
        [constructor]

        Args:
            name ([string]): [book title]
            writer ([string]): [write of the book]
            genre ([string]): [book's genre]
            quantity ([integer]): [number of specific book]
            price ([integer]): [book's price]
        """
        self.name = name
        self.writer = writer
        self.genre = genre
        self.quantity = quantity
        self.price = price
        Book.books_quantity += self.quantity
    
    def book_info(self):
        """
        Prints a general information about a specific book.
        """
        print("Name : ",self.name,
              "Writer : ",self.writer,
              "Book's Genre : ",self.genre,
              "Quantity of this book : ",self.quantity)

    def set_name(self,name):
        Book.name = name
    def set_writer(self,writer):
        Book.writer = writer
    def set_genre(self,genre):
        Book.genre = genre
    def set_quantity(self,bookQuantity):
        Book.bookQuantity = bookQuantity
    def set_price(self,price):
        Book.price = price
 
 
    def get_name(self):
        return self.name 
    def get_writer(self):
        return self.writer
    def get_genre(self):
        return self.genre
    def get_quantity(self):
        return self.quantity
    def get_price(self):
        return self.price
    
    @staticmethod
    def get_books_quantity():
        return Book.books_quantity