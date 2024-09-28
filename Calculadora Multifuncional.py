

def calcular_promedio(num1, num2, num3):
    return (num1 + num2 + num3) / 3

def es_par_o_impar(num):
    return "El número es par" if num % 2 == 0 else "El número es impar"

def calcular_factorial(num):
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado

def calcular_raiz_cuadrada(num):
    return math.sqrt(num)

def calcular_mcm(num1, num2):
    a, b = num1, num2
    while b != 0:
        a, b = b, a % b
    return (num1 * num2) // a

def main():
    print("Calculadora Multifuncional")
    while True:
        print('\nSeleccione una opción:')
        print('1. Calcular promedio de tres números')
        print('2. Verificar si un número es par o impar')
        print('3. Calcular factorial de un número')
        print('4. Calcular raíz cuadrada de un número')
        print('5. Calcular MCM de dos números')
        print('0. Salir')

        opcion = int(input('Opción: '))

        if opcion == 1:
            num1 = float(input('Ingrese el primer número: '))
            num2 = float(input('Ingrese el segundo número: '))
            num3 = float(input('Ingrese el tercer número: '))
            resultado = calcular_promedio(num1, num2, num3)
            print('El promedio es:', resultado)
        
        elif opcion == 2:
            num = int(input('Ingrese un número: '))
            print(es_par_o_impar(num))
        
        elif opcion == 3:
            num = int(input('Ingrese un número: '))
            resultado = calcular_factorial(num)
            print('El factorial es:', resultado)
        
        elif opcion == 4:
            num = float(input('Ingrese un número: '))
            resultado = calcular_raiz_cuadrada(num)
            print('La raíz cuadrada es:', resultado)
        
        elif opcion == 5:
            num1 = int(input('Ingrese el primer número: '))
            num2 = int(input('Ingrese el segundo número: '))
            resultado = calcular_mcm(num1, num2)
            print('El MCM es:', resultado)
        
        elif opcion == 0:
            print('Gracias por usar el programa')
            break
        
        else:
            print('Opción no válida')

if __name__ == "__main__":
    main()