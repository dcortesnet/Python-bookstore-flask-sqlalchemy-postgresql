from flask import Flask

app = Flask(__name__)
port = 5000

@app.route('/')
def hello_world():
    return 'Hello world!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=port)
    print('Server listen on http://localhost:{port}'.format(port))
