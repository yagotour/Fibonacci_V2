#Tarea 1 Yago Touriño Medrano

def fibonacci(longitud):
    num1 = 0
    num2 = 1
    if longitud <= 0:
        return "El número debe ser superior a 0"
    elif longitud == 1:
        return 0
    elif longitud == 2:
        return 1
    else:
        for i in range(longitud - 2):
            resultado = num2+num1
            num1 = num2
            num2 = resultado
        return resultado
print(fibonacci(5))
