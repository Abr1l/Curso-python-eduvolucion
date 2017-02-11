#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
#El módulo os nos permite acceder a funcionalidades dependientes del Sistema Operativo. Sobre todo, aquellas que nos refieren información sobre el entorno del mismo y nos permiten manipular la estructura de directorios (para leer y escribir archivos

import csv

directorio = {}

def mostrar_menu():
	print("1- Imprimir directorio telefónico ")
	print("2- Agregar número telefónico")
	print("3- Eliminar número telefónico")
	print("4- Buscar número telefónico")
	print("5- Guardar directorio telefónico")
	print("6- Salir ")
	print(" ")
	

def mostrarDirectorio():
	print("Números telefónico ")
	for x in directorio.keys():
		print("Nombre: " + x + "\tNúmero: " + directorio[x])
	
def agregarContacto():
	print("Agregar contacto")
	nombre = raw_input("Nombre del contacto: ")
	telefono = raw_input("Número de teléfono: ")
	directorio[nombre] = telefono
	print(" ")

def eliminarContacto():
	print("Eliminar contacto")
	nombre = raw_input ("indica el nombre eliminar: ")
	if nombre in directorio:
		del directorio[nombre]
		print(" ")
	else:
		print("¡El nombre no fue encontrado!")

def buscarContacto():
	print("Buscar contacto")
	nombre = raw_input ("indica el nombre a buscar: ")
	if nombre in directorio:
		print("El número es: " + directorio[nombre])
		print(" ")
	else:
		print("¡" + nombre + " no fue encontrado!")
		print(" ")

def guardarArchivo():
	print("Guardar Archivo")
	if not os.path.exists("directorio.csv"): #os.path.exists saber si existe el archivo
		archivocsv = csv.writer(open("directorio.csv", "wb")) 
		#abre con permiso de escritura, si no existe, lo crea.
		for (clave, valor) in directorio.items(): 
	# items, Obtener las claves y valores de un diccionario
			archivocsv.writerow([clave,valor]) 

