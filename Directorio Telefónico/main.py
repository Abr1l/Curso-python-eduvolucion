#!/usr/bin/env python
#-*- coding:utf-8 -*-

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

import directorio

opcion = 0
while opcion == 6:
	mostrar_menu()
	opcion = int(input("Introduzca la opción:"))
	if opcion == 1:
		directorio.mostrarDirectorio()
	elif opcion == 2:
		directorio.agregarContacto()
	elif opcion == 3:
		directorio.eliminarContacto()
	elif opcion == 4:
		directorio.buscarContacto()
	elif opcion == 5:
		directorio.guardarArchivo()
	elif opcion != 6:
		directorio.mostrarDirectorio()

