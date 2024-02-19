# Implement a class named "Book" with the following attributes.

# Title
# Author
# ISBN (International Standard Book Number)
# Price
# Quantity (number of available copies)
###########################################################################################################
class Book:
    def __init__(self, title, author, ISBN, price, quantity):############### 1.Book Details ################
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Price: {self.price}, Quantity: {self.quantity}"
    
    
    
# Implement a class named "Catalog" to manage the collection of books.
  
# 1.Adding a new book to the catalog.
# 2.Updating the quantity of available copies for a book.
# 3.Searching for a book by its title, author, or ISBN.
# 4.Displaying the list of all available books.
###########################################################################################################
class Catalog:
    def __init__(self): ############# Books list ################
        self.books = []

    def add_book(self, book):   ############### 1.Book Add ################
        self.books.append(book)

    def update_quantity(self, ISBN, new_quantity):  ############### 2.Stock Update ################
        for book in self.books:
            if book.ISBN == ISBN:
                book.quantity = new_quantity
                return True
        return False

    def search_book(self, search_key):  ############### 3.Book Search ################
        results = []
        for book in self.books:
            if search_key.lower() in book.title.lower() or \
               search_key.lower() in book.author.lower() or \
               str(book.ISBN).lower() == search_key.lower():
                results.append(book)
        return results

    def display_books(self):    ############### 4.Books Show ################
        if not self.books:
            print("No books in the catalog!") 
            
        else:
            print("List of Books:")
            for book in self.books:
                print(book)
            
                
                
                
# Implement a class named "Order" to represent a customer order.

# 1.List of books ordered and Calculating the total amount for an order.
# 2.Order History
###########################################################################################################
class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.books_ordered = []
        self.total_amount = 0

    def add_book_to_order(self, book, quantity):    ############### 1.Books Order ################
        self.books_ordered.append((book, quantity))
        self.total_amount += book.price * quantity

    def display_order_summary(self):    ############### 2.Order Summery ################
        print(f"Order Summary for {self.customer_name}:")
        for book, quantity in self.books_ordered:
            print(f"Title: {book.title}, Quantity: {quantity}, Price per unit: {book.price}")
        print(f"Total Amount: {self.total_amount}")

###########################################################################################################
# Implement a class named "Bookstore" to handle customer interactions.

# 1.Displaying the catalog of books.
# 2.Placing a new order with customer name and Updating the quantity of books after an order is placed.
# 3.Displaying the list of all orders received.
###########################################################################################################
class Bookstore:
    def __init__(self):
        self.catalog = Catalog()
        self.orders = []

    def add_book_to_catalog(self):  ############### Adding Book Details ################
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        ISBN = input("Enter the ISBN of the book: ")
        price = float(input("Enter the price of the book: "))
        quantity = int(input("Enter the quantity of the book: "))
        book = Book(title, author, ISBN, price, quantity)
        self.catalog.add_book(book)
        print("Book added to catalog successfully.")

    def display_catalog(self):  ############### 1.Display Catalog of Books ################
        self.catalog.display_books()

    def place_order(self):  ############### 2.Order Placing ################
        customer_name = input("Enter your name: ")
        order = Order(customer_name)
        
        if not self.catalog.books:
            print("There are no books in the catalog. Please come back later!")
            return
        
        self.display_catalog()
        while True:
            ISBN = input("Enter the ISBN of the Book to order or 'done' to finish: ")
            if ISBN.lower() == "done":
                break
            quantity = int(input("Enter the quantity: "))
            books_found = self.catalog.search_book(ISBN)
            if not books_found:
                print("Book not found in catalog.")
                continue
            book = books_found[0]
            if book.quantity < quantity:
                print("Insufficient quantity..\n")
                continue
            order.add_book_to_order(book, quantity)
            self.catalog.update_quantity(ISBN, book.quantity - quantity)

        self.orders.append(order)
        order.display_order_summary()

    def display_orders(self): ############### 3.Order Summery ################
        if not self.orders:
            print("No orders received yet.")
        else:
            print("List of Orders:")
            for i, order in enumerate(self.orders, 1):
                print(f"Order {i}:")
                order.display_order_summary()


def main():
    bookstore = Bookstore()
    print("Welcome to the Online Bookstore!")
    

    while True:
        print("\nMenu:")
        print("1. Add a new book to the catalog")
        print("2. View the catalog of books")
        print("3. Place a new order")
        print("4. View list of order")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        print("\n")
        
        if choice == '1':
            
            bookstore.add_book_to_catalog()
            
        elif choice == '2':
            
            bookstore.display_catalog()
            
        elif choice == '3':
            
            bookstore.place_order()
            
            
        elif choice == '4':
            
            bookstore.display_orders()
            
        elif choice == '5':
            print("Exiting..... Thank You! :)")
            break
        else:
            print("Invalid choice. Please try again.")
            
            
if __name__ == "__main__":
    main() 