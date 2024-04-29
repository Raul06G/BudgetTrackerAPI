from flask import Flask, request

app = Flask(__name__)

brukernavn = "raul"
passord = "hei123"

@app.route('/')
def default():
    return 'Velkomen til vårt nydelijge api'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username != brukernavn:
            return "dra til helvete"
        
        if password != passord:
            return "fuck off"

        return "aproved"


if __name__ == "__main__":
    print("ja")
    app.run()