#Tarea 1 Yago Touriño Medrano
#Archivo .py donde está creada la función "fibonacci" perteneciente al primer punto del ejercicio.

def fibonacci(posicion):
    num1 = 0
    num2 = 1
    if posicion <= 0:
        return "El número debe ser superior a 0"
    elif posicion == 1:
        return 0
    elif posicion == 2:
        return 1
    else:
        for i in range(posicion - 2):
            resultado = num2+num1
            num1 = num2
            num2 = resultado
        return resultado
#print(fibonacci(5))