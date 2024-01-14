from flask import Flask
from models import db

app = Flask(__name__)
port = 5000
app.config['SQLALCHEMY_DATABASE_URI']= 'postgres://postgres:@localhost:5432/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.route('/')
def hello_world():
    return 'Hello world!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=port)
    db.init_app(app)
    print('Server listen on http://localhost:{port}'.format(port))
