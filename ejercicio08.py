#Estilo de python pep8

platillos = ["pollo tipico", "pinchos", "chuleta",
"lasagna", "camarones Empanizados"]

pedidos = []

def imprimir_menu():
	print("1 Mostrar platillos")
	print("2 agregar pedido")
	print("3 imprimir pedidos")
	print("4 eliminar pedidos")
	print("5 salir")
	print("0 alamcenar pedidos")

	valor = int(input("Escriba el numero de la accion que desea realizar "))
	return valor


def mostar_platillos():
	print("listado de platillos Disponibles")

	for platillo in platillos:
		print(platillo)



def agregar_pedido():
	plato = input("escriba el plato que desea ")

	cantidad = int(input("escriba la cantidad de platillos que desea"))

	mesa = int(input("escriba el numero de la mesa"))
	
	pedido = "{0}, cantidad: {1}, mesa:{2}".format(plato, cantidad, mesa)
	
	pedidos.append(pedido)


def mostrar_pedidos():
	print("listado de pedidos pendientes")

	for pedido in pedidos:
		print(pedido)


def eliminar_pedidos():
	pedidos = [] 

	print("se eliminaron todos los pedidos")

def alamcenar():
	f = open("pedidos.txt", "w+")
	for pedido in pedidos:
		f.write(" {0} \n".format(pedidos))

continuar = True 

while continuar:
	accion = imprimir_menu()
	if accion == 1:
		mostar_platillos()
	elif accion == 2:
		agregar_pedido()
	elif accion == 3:
		mostrar_pedidos()
	elif accion == 4:
		eliminar_pedidos()
	elif accion == 5:
		continuar = False 
	elif accion == 0:
		almacenar()
	else:
		print("Accion desconocida ") 
