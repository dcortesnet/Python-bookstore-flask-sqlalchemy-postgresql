from flask import Flask, request, jsonify
from models import db, Author, Book

app = Flask(__name__)
port = 5000
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://postgres:123456@localhost:5432/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/authors', methods=['GET'])
def get_authors():
    try:
        authors = Author.query.all()
        authors_data = []
        for author in authors:
            author_data = {
                'id': author.id,
                'name': author.name,
                'age': author.age,
                'books': []
            }
            for book in author.books:
                book_data = {
                    'id': book.id,
                    'isbn': book.isbn,
                    'name': book.name,
                    'cant_pages': book.cant_pages,
                    'createdAt': book.created_at
                }
                author_data['books'].append(book_data)
            authors_data.append(author_data)
        return jsonify({'authors': authors_data})
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500

@app.route('/authors', methods=['POST'])
def add_author():
    try:
        data = request.json
        name = data.get('name')
        age = data.get('age')
        if not name or not age:
            return jsonify({'message': 'Bad request, name or age not found'}), 400
        new_author = Author(name=name, age=age)
        db.session.add(new_author)
        db.session.commit()
        return jsonify({'author': {'id': new_author.id, 'name': new_author.name, 'age': new_author.age}}), 201
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500

@app.route('/books', methods=['GET'])
def get_books():
    try:
        books = Book.query.all()
        books_data = []
        for book in books:
            book_data = {
                'id': book.id,
                'isbn': book.isbn,
                'name': book.name,
                'cant_pages': book.cant_pages
            }
            books_data.append(book_data)
        return jsonify({'books': books_data})
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500

@app.route('/books', methods=['POST'])
def add_book():
    try:
        data = request.json
        isbn = data.get('isbn')
        name = data.get('name')
        cant_pages = data.get('cant_pages')
        author_id = data.get('author')
        if not name or not cant_pages or not author_id or not isbn:
            return jsonify({'message': 'Bad request, isbn or name or cantPages or author not found'}), 400
        new_book = Book(isbn=isbn, name=name, cant_pages=cant_pages, author_id=author_id)
        db.session.add(new_book)
        db.session.commit()
        return jsonify({'book': {'id': new_book.id, 'isbn': new_book.isbn, 'name': new_book.name, 'cant_pages': new_book.cant_pages}}), 201
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)
