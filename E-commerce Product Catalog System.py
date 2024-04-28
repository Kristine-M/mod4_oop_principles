class Product:
    # Constructor and common attributes
    def __init__(self, id, item_name, price):
        self.id = id
        self.itemName = item_name
        self.price = price

    def display_info(self):
        # General method to display product info
        print("Product:", self.itemName, "\nPrice: ", self.price)

class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def author(self):
        print("The", self.itemName, "is written by", self.author)
        
    def display_info(self):
        print("The", self.itemName, "is ", self.price, "and is written by", self.author)
        
class Electronic(Product):
    def __init__(self, product_id, name, price, res):
        super().__init__(product_id, name, price)
        self.res = res

    def electr(self):
        print("The", self.itemName, "has a", self.res, "resolution")
        
        
    def display_info(self):
        # Overridden method for books
        print("The", self.itemName, "is ", self.price, "and has a", self.res, "resolution")

class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size


    def clothes(self):
        print("This", self.itemName, "is a size", self.size)
        
    def display_info(self):
        # Overridden method for books
        print("This", self.itemName, "is ", self.price, "and is a size", self.size)
        
        
# Example usage
my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
my_book.display_info()

leggings = Clothing("345", "leggings", "50.99", "medium")
leggings.clothes()
leggings.display_info

phone = Electronic("678", "iPhone 14", "999.99", "1080p")
phone.electr()
phone.display_info