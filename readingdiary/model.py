from datetime import datetime

class Note:
    def __init(self, text: str, page: int, date: datetime  ):
        self.text = text
        self.page = page
        self.date = date

    def __str__(self):
        return f"{self.text} {self.page} {self.date}"

class Book:
    EXCELLENT = 3
    GOOD = 2
    BAD = 1
    UNRATED = -1

    def __init__(self, isbn : str, title: str, author: str, pages: int):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.pages = pages

