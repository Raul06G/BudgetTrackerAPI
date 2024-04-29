from flask import Flask, request

app = Flask(__name__)

brukernavn = "raul"
passord = "hei123"

@app.route('/')
def default():
    return 'Velkomen til vårt nydelijge api'

@app.route('/loginpage')
def loginpage():
    return '''
        <h1>velkomen til login</h1>
        <form>
            <input>Brukernavn</input> <br/>
            <input>Passord</input> <br />
            <button onclick="hei()"><a href="result">hei</a></button>
            <button onclick="hei()">Hei</button>
        </form>

        <script>
            funtion hei() {
                //login
                console.log("hello world);
                //window.location.href = "https://vg.no";
            }
        </script>
    '''

@app.route('/result')
def ressult():
    return '''<h1>loged in</h1>'''


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