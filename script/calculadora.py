def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "No se puede dividir entre 0"
    return a / b


print("=== Mi Calculadora DevOps ===")

a = float(input("Introduce el primer número: "))
operacion = input("Operación (+, -, *, /): ")
b = float(input("Introduce el segundo número: "))

if operacion == "+":
    resultado = sumar(a, b)
elif operacion == "-":
    resultado = restar(a, b)
elif operacion == "*":
    resultado = multiplicar(a, b)
elif operacion == "/":
    resultado = dividir(a, b)
else:
    resultado = "Operación no válida"

print(f"Resultado: {resultado}")