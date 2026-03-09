from datetime import datetime
from typing import List


class Note:
    def __init(self, text: str, page: int, date: datetime):
        self.text :str = text
        self.page :int = page
        self.date :datetime = date

    def __str__(self):
        return f"{self.text} {self.page} {self.date}"

class Book:
    EXCELLENT = 3
    GOOD = 2
    BAD = 1
    UNRATED = -1

    def __init__(self, isbn : str, title: str, author: str, pages: int):
        self.isbn :str = isbn
        self.title :str = title
        self.author :str = author
        self.pages :int = pages
        self.rating :int = Book.UNRATED
        self.notes :List[Note] = []

    def add_note(self, text : str, page : int, date: datetime)-> bool:
        if page > self.pages:
            return False
        else:
            note = Note(text, page, date)
            self.notes.append(note)
            return True

    def set_rating(self, rating : int)-> bool:
        if rating not in (Book.EXCELLENT, Book.GOOD, Book.BAD):
            return False
        else:
            self.rating = rating
            return True

    def get_notes_of_page(self, page: int) -> List[Note]:
        notes_of_page: List[Note] = []
        for note in self.notes:
            if note.page == page:
                notes_of_page.append(note)
        return notes_of_page






