# src/PythonCalculator.py

class PythonCalculator:
    def sumar(self, x, y):
        return x + y

    def restar(self, x, y):
        return x - y

    def multiplicar(self, x, y):
        return x * y

    def dividir(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y