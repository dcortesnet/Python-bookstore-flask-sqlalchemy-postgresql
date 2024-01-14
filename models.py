from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime)
    books = db.relationship("Book")

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    cant_pages = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.datetime)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))