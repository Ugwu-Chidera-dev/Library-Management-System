from datetime import datetime
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, contact_info):
        self.name = name
        self.age = age
        self.contact_info = contact_info

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            if value.strip():
                self._name = value.strip()
            else:
                raise ValueError("Name cannot be empty")
        else:
            raise TypeError("Name must be a string")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and not isinstance(value, bool):
            if value > 0:
                self._age = value
            else:
                raise ValueError("Age must be positive")
        else:
            raise TypeError("Age must be an integer")

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if isinstance(value, str):
            if value.strip():
                self._contact_info = value.strip()
            else:
                raise ValueError("Contact info cannot be empty")
        else:
            raise TypeError("Contact info must be a string")

    @abstractmethod
    def introduce(self):
        pass

class Book:
    def __init__(self, isbn, title, author, publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self._availability = True

    @staticmethod
    def is_isbn_valid_10(value):
        if value.isdigit() or (value[9] == "X" and value[:9].isdigit()):
            total = 0
            number = 10
            for i in value[:9]:
                total += int(i) * number
                number -= 1
            if value[9] == "X":
                total += 10
            else:
                total += int(value[9])
            if total % 11 == 0:
                return True
        return False

    @staticmethod
    def is_isbn_valid_13(value):
        if value.isdigit():
            total = 0
            for index, i in enumerate(value[:12]):
                if (index + 1) % 2 == 0:
                    total += int(i) * 3
                else:
                    total += int(i) * 1
            ans = 10 - (total % 10)
            if ans == 10:
                ans = 0
            if ans == int(value[12]):
                return True
        return False

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        if isinstance(value, str) and value.strip():
            new_value = value.strip().replace("-", "")
            if len(new_value) == 13:
                if self.is_isbn_valid_13(new_value):
                    self._isbn = new_value
                else:
                    raise ValueError("ISBN must be valid")
            elif len(new_value) == 10:
                if self.is_isbn_valid_10(new_value):
                    self._isbn = new_value
                else:
                    raise ValueError("ISBN must be valid")
            else:
                raise ValueError("ISBN must be a 10 or 13 digit ISBN")
        else:
            raise TypeError("ISBN must be a string and not be empty")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str):
            if value.strip():
                self._title = value.strip()
            else:
                raise ValueError("Title cannot be empty")
        else:
            raise TypeError("Title must be a string")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, str):
            if value.strip():
                self._author = value.strip()
            else:
                raise ValueError("Author cannot be empty")
        else:
            raise TypeError("Author must be a string")

    @property
    def publication_year(self):
        return self._publication_year

    @publication_year.setter
    def publication_year(self, value):
        if isinstance(value, int) and not isinstance(value, bool):
            current_year = int(datetime.now().strftime("%Y"))
            if 1000 <= value <= current_year:
                self._publication_year = value
            else:
                raise ValueError("Publication year must be between 1000 and current year")
        else:
            raise TypeError("Publication year must be an integer")

    @property
    def availability(self):
        return self._availability

    def borrow(self):
        if self._availability:
            self._availability = False
        else:
            raise ValueError("Book isn't available for borrow at the moment")

    def return_book(self):
        if self._availability:
            raise ValueError("Book has already been returned to the catalogue")
        else:
            self._availability = True

    def __str__(self):
        return f"Title: {self.title} by {self.author}\nISBN: {self.isbn}\nPublication Year: {self.publication_year}"

class Member(Person):
    def __init__(self, name, age, contact_info, member_id):
        super().__init__(name, age, contact_info)
        self.member_id = member_id
        self._member_status = "active"

    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        if isinstance(value, str):
            value = value.strip()
            if value:
                if value.startswith("MID-") and value[4:7].isdigit() and len(value) == 7:
                    self._member_id = value
                else:
                    raise ValueError("Member ID must follow the format <MID-000>")
            else:
                raise ValueError("Member ID must not be empty")
        else:
            raise TypeError("Member ID must be a string")

    @property
    def member_status(self):
        return self._member_status

    def activate(self):
        self._member_status = "active"

    def deactivate(self):
        self._member_status = "inactive"

    def introduce(self):
        return f"Name: {self.name}\nAge: {self.age}\nMember ID: {self.member_id}\nMembership Status: {self.member_status}"

    def __str__(self):
        return f"Name: {self.name}\nMember ID: {self.member_id}\nMembership Status: {self.member_status}"

class Librarian(Person):
    def __init__(self, name, age, contact_info, librarian_id):
        super().__init__(name, age, contact_info)
        self.librarian_id = librarian_id
        self._employment_status = "active"

    @property
    def librarian_id(self):
        return self._librarian_id

    @librarian_id.setter
    def librarian_id(self, value):
        if isinstance(value, str):
            value = value.strip()
            if value:
                if value.startswith("LID-") and value[4:7].isdigit() and len(value) == 7:
                    self._librarian_id = value
                else:
                    raise ValueError("Librarian ID must follow the format <LID-000>")
            else:
                raise ValueError("Librarian ID must not be empty")
        else:
            raise TypeError("Librarian ID must be a string")

    @property
    def employment_status(self):
        return self._employment_status

    def activate(self):
        self._employment_status = "active"

    def deactivate(self):
        self._employment_status = "inactive"

    def introduce(self):
        return f"Name: {self.name}\nContact Info: {self.contact_info}\nLibrarian ID: {self.librarian_id}\nEmployment Status: {self.employment_status}"

    def __str__(self):
        return f"Name: {self.name}\nLibrarian ID: {self.librarian_id}\nEmployment Status: {self.employment_status}"

class BorrowRecord:
    def __init__(self, member, book):
        self.member = member
        self.book = book
        self._borrowed_at = datetime.now()
        self._returned_at = None

    @property
    def member(self):
        return self._member

    @member.setter
    def member(self, value):
        if isinstance(value, Member):
            self._member = value
        else:
            raise TypeError("Member must be a Member object")

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if isinstance(value, Book):
            self._book = value
        else:
            raise TypeError("Book must be a Book object")

    @property
    def borrowed_at(self):
        return self._borrowed_at

    @property
    def returned_at(self):
        return self._returned_at

    def mark_returned(self):
        if self._returned_at is None:
            self._returned_at = datetime.now()
        else:
            raise ValueError("Book record has been not returned")

class Library:
    def __init__(self):
        self._books = []
        self._members = []
        self._librarians = []
        self._borrow_records = []

    @property
    def books(self):
        return self._books.copy()

    @property
    def members(self):
        return self._members.copy()

    @property
    def librarians(self):
        return self._librarians.copy()

    @property
    def borrow_records(self):
        return self._borrow_records.copy()

    def _find_member(self, value):
        for member in self._members:
            if value == member.member_id:
                return member
        return None

    def _find_book(self, value):
        for book in self._books:
            if value == book.isbn:
                return book
        return None

    def _find_librarian(self, value):
        for librarian in self._librarians:
            if value == librarian.librarian_id:
                return librarian
        return None

    def add_book(self, value):
        if isinstance(value, Book):
            book = self._find_book(value.isbn)
            if book is not None:
                raise ValueError("Book already exist")
            self._books.append(value)
        else:
            raise TypeError("Book must be a Book object")

    def add_member(self, value):
        if isinstance(value, Member):
            member = self._find_member(value.member_id)
            if member is not None:
                raise ValueError("Member already exists")
            self._members.append(value)
        else:
            raise TypeError("Member must be a Member object")

    def add_librarian(self, value):
        if isinstance(value, Librarian):
            librarian = self._find_librarian(value.librarian_id)
            if librarian is not None:
                raise ValueError("Librarian already exists")
            self._librarians.append(value)
        else:
            raise TypeError("Librarian must be a Librarian object")

    def _find_active_borrow_record_for_book(self, book):
        for record in self._borrow_records:
            if book is record.book:
                if record.returned_at is None:
                    return record
        return None

    def _find_active_borrow_record_for_member(self, member):
        for record in self._borrow_records:
            if member is record.member:
                if record.returned_at is None:
                    return record
        return None

    def remove_book(self, isbn):
        book = self._find_book(isbn)
        if book is not None:
            if self._find_active_borrow_record_for_book(book) is None:
                self._books.remove(book)
            else:
                raise ValueError("Book has not been returned")
        else:
            raise ValueError("Book does not exist")

    def remove_member(self, member_id):
        member = self._find_member(member_id)
        if member is not None:
            if self._find_active_borrow_record_for_member(member) is None:
                self._members.remove(member)
            else:
                raise ValueError("Member has not returned borrowed book")
        else:
            raise ValueError("Member does not exist")

    def remove_librarian(self, librarian_id):
        librarian = self._find_librarian(librarian_id)
        if librarian is not None:
                self._librarians.remove(librarian)
        else:
            raise ValueError("Librarian does not exist")

    def borrow_book(self, member_id, isbn):
        member = self._find_member(member_id)
        book = self._find_book(isbn)
        if member is not None:
            if member.member_status == "active":
                if book is not None:
                    if book.availability:
                        book.borrow()
                        try:
                            record = BorrowRecord(member, book)
                        except TypeError:
                            book.return_book()
                            raise
                        else:
                            self._borrow_records.append(record)
                    else:
                        raise ValueError("Book is not available")
                else:
                    raise ValueError("Book does not exist")
            else:
                raise ValueError("Membership is not active")
        else:
            raise ValueError("Member does not exist")

    def _find_active_borrow_record(self, member, book):
        for record in self._borrow_records:
            if record.book is book and record.member is member and record.returned_at is None:
                return record
        return None

    def return_book(self, member_id, isbn):
        member = self._find_member(member_id)
        book = self._find_book(isbn)
        if member is None:
            raise ValueError("Member does not exist")
        if member.member_status != "active":
            raise ValueError("Membership is not active")
        if book is None:
            raise ValueError("Book does not exist")
        if book.availability:
            raise ValueError("Book is not available")
        record = self._find_active_borrow_record(member, book)
        if record is None:
            raise ValueError("Book has been returned")
        book.return_book()
        try:
            record.mark_returned()
        except ValueError:
            book.borrow()
            raise

    def search_book(self, isbn):
        book = self._find_book(isbn)
        return book

    def search_member(self, member_id):
        member = self._find_member(member_id)
        return member

    def search_librarian(self, librarian_id):
        librarian = self._find_librarian(librarian_id)
        return librarian

    def get_active_borrow_records(self):
        active_borrow_records = []
        for record in self._borrow_records:
            if record.returned_at is None:
                active_borrow_records.append(record)
        return active_borrow_records

# library = Library()
#
# book1 = Book("9780306406157", "Avatar", "James Griffin", 2010)
# book2 = Book("0306406152", "Solo Leveling", "Kyoto Osuma", 2016)
#
# member1 = Member("Chidera Valentine", 20, "ugwuchidera@gmail.com", "MID-002")
# member2 = Member("Daniel Creed", 19, "danielcreed@outlook.com", "MID-004")
#
# librarian = Librarian("James Jackson", 36, "jacksonjames@yahoo.com", "LID-001")
#
# library.add_book(book1)
# library.add_book(book2)
# library.add_member(member1)
# library.add_member(member2)
# library.add_librarian(librarian)
#
# library.borrow_book("MID-002", "9780306406157")
# library.borrow_book("MID-004", "0306406152")
#
# print(book1.availability)
# print(book2.availability)
#
# print(library.get_active_borrow_records())
#
# try:
#     library.borrow_book("MID-004", "0306406152")
# except ValueError as e:
#     print(e)
#
# library.return_book("MID-002", "9780306406157")
# print(book1.availability)
# print(book2.availability)
#
# print(library.get_active_borrow_records())
# for book in library.get_active_borrow_records():
#     print(book.returned_at)
#
# print(library.search_book("9780306406157"))
# print(library.search_member("MID-002"))
# print(library.search_librarian("LID-001"))
#
# # library.remove_book("0306406152")
#
# try:
#     library.return_book("MID-002", "0306406152")
# except ValueError as e:
#     print(e)
#
# for record in library.borrow_records:
#     try:
#         if book1 == record.book:
#             print(record.returned_at)
#     except ValueError as e:
#         print(e)
