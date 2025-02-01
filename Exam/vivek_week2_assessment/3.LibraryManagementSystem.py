# •	3. You are building a Library Management System. Create a `Book` class with properties 
# like `title`, `author`, and `isbn`. Write a method to display book details.
class Book:
    def __init__(self,title:str,author:str,isbn:str)->None:
        self.title=title
        self.author=author
        self.isbn=isbn

    def bookDetails(self):
        print(f"The book name is {self.title} author is {self.author} and the isbn: {self.isbn}")


title,author,isbn=map(str,input("Enter title, author, isbn number of the book:").split())
book1=Book(title,author,isbn)
book1.bookDetails()