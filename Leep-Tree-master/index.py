from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Principal.html")

@app.route("/about")
def about():
    return render_template("Home.html")

@app.route("/Tu_Arbol")
def Tu_Arbol():
    return render_template("Tu_Arbol.html")

@app.route("/Desempeño")
def Desempeño():
    return render_template("Desempeño.html")

@app.route("/Lista")
def Lista():
    return render_template("Lista.html")

if __name__ == "__main__":
    app.run(debug=True)

