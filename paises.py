#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Cobertura Telefónica
En este proyecto estarán creando un programa que se encargará de controlar la cobertura telefónica de una empresa que provee
servicios de llamadas internacionales.
Para lograrlo, seguirán las siguientes instrucciones:
• Crearán un diccionario que almacene el nombre de los países y sus abreviaturas: paises.
• Crearán un diccionario que almacene la abreviatura del país y su prefijo telefónico: codigo.
• Imprimirán la lista de países incluidos en la cobertura telefónica.
• Solicitarán el nombre del país, para traer su prefijo telefónico.
• Imprimirán el siguiente mensaje
El prefijo telefónico de Panama (PA) es +507.
Solicitarán, a manera de recomendación, el nombre de un país que no esté en la lista.
Imprimirán un mensaje de agradecimiento.
Tendrán que utilizar los conceptos aprendidos en este capítulo: listas, tuplas y diccionarios. Además de los conceptos que se vieron
en los capítulos anteriores. '''

#Diccionario de paises
paises = {
	"Panama":"PA",
	"Colombia":"CO",
	"Venezuela":"VE",
	"Ecuador":"EC", 
	"Argentina":"AR"
}

#Diccionario de abreviatura de paises con el código
codigo = {
	"PA":"+507",
	"CO":"+57",
	"VE":"+58",
	"EC":"+593",
	"AR":"+54"
}

print("Paises con Cobertura Internacional")
print("---"*23)
print("Lista de paises:" + str(paises.keys()))

x = raw_input("\n Escriba el nombre del país: ")
print("\nEl prefijo telefónico de " + x + " (" + paises[x] +") es " + codigo[paises[x]]  + ".")

print("---" * 23)
print("---" * 23)
print("Recomendaciones")

paises_posibles = []
pais = raw_input("\n ¿Qué pais recomienda darle cobertura?  ")
paises_posibles.append(pais)
print("\n Gracias por su cooperación, esperamos que " + paises_posibles[0] + " sea incluido")









