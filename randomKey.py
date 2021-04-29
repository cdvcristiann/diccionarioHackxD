import random
import os

dic = open("D:/Kali/diccionario.txt","w")
letras="wlan"
listaLetras="abecdefghijklmnopkrstuvwxz1234567890"


def seleccion_palabra(lista):
	palabra=list(random.choice(lista))
	return palabra

def codwlan(lista, letras):
	for x in listaLetras:
		palabra= seleccion_palabra(listaLetras)
		for x in palabra:
			letras+=x
		if len(letras) == 10:
			dic.write(letras + "\n")
			break


cantcod = 0
while cantcod < 200000:
	cod = codwlan(listaLetras, letras)
	cantcod+=1


dic.close()
