class Book:
    def __init__(self, title, author, ISBN, price, quantity):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Price: {self.price}, Quantity: {self.quantity}"


class Catalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def update_quantity(self, ISBN, new_quantity):
        for book in self.books:
            if book.ISBN == ISBN:
                book.quantity = new_quantity
                return True
        return False

    def search_book(self, search_key):
        results = []
        for book in self.books:
            if search_key.lower() in book.title.lower() or \
               search_key.lower() in book.author.lower() or \
               str(book.ISBN).lower() == search_key.lower():
                results.append(book)
        return results

    def display_books(self):
        if not self.books:
            print("No books in the catalog!")
        else:
            print("List of Books:")
            for book in self.books:
                print(book)


class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.books_ordered = []
        self.total_amount = 0

    def add_book_to_order(self, book, quantity):
        self.books_ordered.append((book, quantity))
        self.total_amount += book.price * quantity

    def display_order_summary(self):
        print(f"Order Summary for {self.customer_name}:")
        for book, quantity in self.books_ordered:
            print(f"Title: {book.title}, Quantity: {quantity}, Price per unit: {book.price}")
        print(f"Total Amount: {self.total_amount}")


class Bookstore:
    def __init__(self):
        self.catalog = Catalog()
        self.orders = []

    def add_book_to_catalog(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        ISBN = input("Enter the ISBN of the book: ")
        price = float(input("Enter the price of the book: "))
        quantity = int(input("Enter the quantity of the book: "))
        book = Book(title, author, ISBN, price, quantity)
        self.catalog.add_book(book)
        print("Book added to catalog successfully.")

    def display_catalog(self):
        self.catalog.display_books()

    def place_order(self):
        customer_name = input("Enter your name: ")
        order = Order(customer_name)

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

    def display_orders(self):
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