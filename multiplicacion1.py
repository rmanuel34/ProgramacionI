print("tabla del 2")
for elemento in range(1,11):
    resultado = 2 * elemento
    print("2 x {0} = {1}".format(elemento,resultado))
print()


print("tabla del 4")
for elemento in range(1,11):
    resultado = 4 * elemento
    print("4 x {0} = {1}".format(elemento,resultado))
print()


print("tabla del 23")
for elemento in range(1,11):
    resultado = 23 * elemento
    print("23 x {0} = {1}".format(elemento,resultado))
print()

print("tabla del 76")
for elemento in range(1,11):
    resultado = 76 * elemento
    print("76 x {0} = {1}".format(elemento,resultado))
print()

for indice in range (32,36):
    print("tabla del ",indice)
    for elemento in range(1,11):
        resultado = indice * elemento
        print("{2} x {0} = {1}".format(elemento,resultado,indice))
    print()

print()
print("otros valores")
print()

tablas= [21, 34, 54, 65, 76]
for indice in tablas:
    print("tabla del ", indice)
    for elemento in range(1,11):
        resultado = indice * elemento
        print("{2} x {0} = {1}".format(elemento,resultado,indice))
    print()


    
