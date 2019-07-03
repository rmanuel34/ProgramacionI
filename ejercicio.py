productos = ["coca cola", "Fanta", "Fresca", " Dassani"]

def imprimir_menu():
	print("1 Mostrar el productos")
	print("2 Eliminar productos")
	print("3 Agregar producto")
	print("4 salir")
	valor= input("ingrese el de la accion: ")
	return valor

salir= True

while continuar:
	#v_retornado = valor retornado
	v_retornado = imprimir_menu()
	if int(v_retornado) == 1 :
		for producto in productos:
			print(producto)
	elif int(v_retornado) == 2 :
		productos = []
	elif int(v_retornado) == 3 :
		valor = input(ingrese el producto a agregar: ")
		productos . append(valor)
	elif int(V_retornado) == 4 :
		continuar = false 
	else:
		print("opcion no controlada")
