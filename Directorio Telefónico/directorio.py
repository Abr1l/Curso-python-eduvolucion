#Directorio Telefónico
#En este proyecto estarán creando un programa que simulará un directorio telefónico.
#El programa debe cumplir con los siguientes objetivos:
#• Crear un directorio telefónico usando un diccionario.
#• Imprimir la lista de contactos de mi directorio telefónico.
#• Agregar, eliminar y buscar contactos dentro de mi directorio telefónico.
#• Guardar mi directorio telefónico en un fichero llamado directorio.csv.
#• Toda la lógica de la aplicación estará disponible en un módulo llamado directorio.py.
#• La integración final estará disponible en un fichero llamado main.py.
#Tendrán que utilizar la mayor parte de los conceptos aprendidos a lo largo de este capítulo: módulos, errores y excepciones,
#entrada y salida de ficheros. Además de los conceptos aprendidos en los capítulos anteriores



import csv
directorio = {}

def mostrar_menu():
	print("1- Imprimir directorio telefónico ")
	print("2- Agregar número telefónico")
	print("3- Eliminar número telefónico")
	print("4- Buscar número telefónico")
	print("5- Importar a un archivo csv el directorio telefónico")
	print("6- Salir ")
	

def imprimirDirectorio():
	print("Números telefónico ")
	for x in directorio.keys():
		print("Nombre: " + x + "\tNúmero: " + directorio[x])
		print()
	
	
