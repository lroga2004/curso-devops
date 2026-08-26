from flask import Flask, render_template, request
from calculadora import sumar, restar, multiplicar, dividir

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculadora():
    resultado = None

    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        operacion = request.form["operacion"]

        if operacion == "+":
            resultado = sumar(a, b)
        elif operacion == "-":
            resultado = restar(a, b)
        elif operacion == "*":
            resultado = multiplicar(a, b)
        elif operacion == "/":
            resultado = dividir(a, b)

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)