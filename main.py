# main.py

import sys
sys.path.append('./src')

from PythonCalculator import PythonCalculator

def main():
    calc = PythonCalculator()

    print("Selecciona la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    eleccion = input("Introduce tu elección (1/2/3/4): ")

    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if eleccion == '1':
        print(f"Resultado: {calc.sumar(num1, num2)}")
    elif eleccion == '2':
        print(f"Resultado: {calc.restar(num1, num2)}")
    elif eleccion == '3':
        print(f"Resultado: {calc.multiplicar(num1, num2)}")
    elif eleccion == '4':
        try:
            print(f"Resultado: {calc.dividir(num1, num2)}")
        except ValueError as e:
            print(e)
    else:
        print("Elección no válida")

if __name__ == '__main__':
    main()