class LibraryBook:
    def __init__(self, title, book_id, access_code):
        self.title = title             # Public
        self._book_id = book_id        # Protected
        self.__access_code = access_code # Private

    def show_book(self):
        print("Title:", self.title)
        print("Book ID:", self._book_id)
        print("Access Code:", self.__access_code)

book = LibraryBook("Python Basics", "BK101", "LIB999")

print(book.title)
print(book._book_id)
# print(book.__access_code)

book.show_book()