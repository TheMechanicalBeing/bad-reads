from src.extensions import db
from src.models import BaseModel


class Category(db.Model, BaseModel):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name_ = db.Column(db.String, unique=True)

    books = db.relationship('Book', secondary="categories_books", back_populates="categories")

    def __init__(self, name):
        self.name_ = name

    def __repr__(self):
        return f'<Category: {self.name}>'

    @property
    def name(self):
        return self.name_

    @name.setter
    def name(self, value):
        self.name_ = value.lower()


class CategoryBook(db.Model, BaseModel):
    __tablename__ = 'categories_books'

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))

    def __init__(self, category_id, book_id):
        self.category_id = category_id
        self.book_id = book_id
