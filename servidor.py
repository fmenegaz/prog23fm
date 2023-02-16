from flask import Flask
app = Flask(__name__)
@app.route("/")
def oi():
    return "<b> Bom dia </b> <br> <p> oi professor </p>"
app.run(debug = True)
