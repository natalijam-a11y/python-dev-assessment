class Book:

    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        current_year = 2026
        return current_year - self.publication_year
    
    def get_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"
    



if __name__ == "__main__":

        book1 = Book("Harry Potter and the Philosopher's Stone", "J.K.Rowling", "9780747532743", 1997)

        book2 = Book("The Atheism", "Milan Vukomanovic", "9788679983477", 2019)

        book3 = Book("A Man Called Ove", "Fredrik Backman", "9781476738024", 2012)

        books = [book1, book2, book3]

        for book in books:
            print(book.get_summary())
            print(f"Age: {book.get_age()} years")

           