from flask import Flask

app = Flask(__name__)
message = 'Hello World'
@app.route("/")
def pagina_inicial():
    return message

if __name__ == '__main__':
    app.run(debug=True)