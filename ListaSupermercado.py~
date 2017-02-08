#!/usr/bin/env python
#-*- coding:utf-8 -*-

#Lista de Supermercados
#En este proyecto estarán creando un programa que se encargará de administrar una lista de supermercados.
#Para lograrlo, seguirán las siguientes instrucciones:
#• Crearán una variable que almacene nuestra lista de supermercados: supermercado.
#• Crearán un menú que contendrá las siguientes opciones:
#MENU PRINCIPAL
#1 | Imprimir lista
#2 | Agregar articulo a la lista
#3 | Eliminar articulo especifico
#4 | Imprimir una parte de lista
#5 | Salir
#•
#•
#•
#Crearán una variable que almacenará la opción a elegir del menú: opción.
#El flujo de ejecución de la aplicación debe estar en un ciclo while.
#Para controlar la condición del ciclo, utilizarán una variable bandera: menu.
#En la opción 1, deberán imprimir los artículos de la lista junto a su respectivo índice.
#En la opción 2, se solicitará el nombre del artículo a ingresar y se incluirá en la lista.
#En la opción 3, se especificará el índice del artículo a borrar y se eliminará el mismo de la lista.
#En la opción 4, se especificará el índice del último artículo a imprimir y se mostrarán en pantalla.
#En la opción 5, se mostrará un mensaje de despedida y se terminará la aplicación.
#En caso tal no se cumpla ninguna de las opciones anteriores, debe mostrar un mensaje de error.
#Tendrán que utilizar la mayor parte de los conceptos aprendidos a lo largo de este capítulo: ciclos y decisiones. Además, aplicar los
#conceptos aprendidos en capítulos anteriores.


supermercado = []
menu = False 

while menu == False:
	print("*" * 20)
	print("** MENU PRINCIPAL ** ")
	print("*" * 20)
	print("1 | Imprimir lista")
	print("2 | Agregar articulo a la lista")
	print("3 | Eliminar articulo específico")
	print("4 | Imprimir una parte de lista")
	print("5 | Salir")
	
	opcion = int(input("Eliga una opción: ")) 
	
	if (opcion == 1):
		print("En tu lista de supermercado tienes: ")
		i = 0
		for articulo in supermercado:
			print(str(i) + "\t" + articulo)
			++i
	
	elif (opcion == 2):
		articulo = input("\n¿Qué artículo desea agregar?: ")
		supermercado.append(articulo)
	
	elif (opcion == 3):
		articulo = input("¿Qué artículo desea eliminar?")
		del (supermercado[articulo])
	
	elif (opcion == 4):
		fin = int(input("Ingrese un número, artículo final: "))
		for articulo in range(fin):
			print("supermercado[articulo]")
	
	elif (opcion == 5):
		print("\n ¡Hasta Luego, gracias por su compra!")
		break
	
	else:
		print("Error: Introduzca una opción válida")
	
