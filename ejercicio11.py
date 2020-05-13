# Muestra los divisores de un numero dado (todos)

cont = 0
lista = [1]

n = int(input("Introduzca un numero mayor de 0 para calcular sus divisores:"))
if n<=0:
    print("Introduzca un numero mayor que 0")
else:
    for i in range(2,n+1):
        if n%i == 0:
            cont = cont+1
            lista.append(i)
    print("Estos son los divisores",lista[0:cont+1])