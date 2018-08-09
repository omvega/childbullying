import modulos
import os
import csv, operator
import nltk
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
import collections

from time import time

stemmer = nltk.SnowballStemmer('spanish')
############################################################
 
print ("\n--------AFECTOS PREDOMINANTES EN ORACIONES--------")

############################################################

cadena = ""
cant_palabras_sin_sw = 0
cant_palabras_con_sw = 0
afectocsv = ['afecto/alegria.txt', 'afecto/asco.txt', 'afecto/enojo.txt', 'afecto/miedo.txt', 
	'afecto/sorpresa.txt', 'afecto/tristeza.txt'
	]

agresor_array = []
victima_array = []
total_words = 0
afecto = [0, 0, 0, 0, 0, 0] # contiene la cantidad de palabras de acuerdo a los afectos de "afectoscsv"
# alegría, asco, enojo, miedo, sorpresa, tristeza
# función que cuenta las palabras de una frase
def count_words(cadena):
	num = 0 # contador iniciado en cero
	for word in cadena: # revisa cada palabra de una frase
		num += 1 # por cada palabra dentro de una frase suma 1 al contador
	return num # retorna la cantidad de palabras que contiene la frase

#########################################################################
# indica en qué afecto se encuentra la palabra
def affect_analysis(cadena):
	total_words = 0
	afecto_individual = [0, 0, 0, 0, 0, 0] # afectos por cada frase
	count_bad_words = 0 # cantidad de bad words por frase
	for palabra in cadena: # cada palabra en la frase
		if modulos.bad_words(palabra) == -1: # si es bad word suma uno
			count_bad_words = count_bad_words +1 # suma 1 al contador de bad words
		#########################################################
		for i in range(0, 6): # recorre cada archivo de "afectoscsv"
			if (modulos.affect(palabra, afectocsv[i]) == -2): # si recibe "-2" indica que se encontró y lo agrega al array al afecto correspondiente
				afecto[i] += 1 # contabiliza el elemento
				afecto_individual[i] += 1
			total_words = total_words+afecto[i]
		#########################################################
	if((len(cadena)-4) <= 0):
		return 0
	# si enojo es mayor al 15% de la frase y la frase contiene un 20% o más de bad words
	# se le resta 3 debido a que uno es la fecha, la hora y el nombre de quien escribe el mensaje
	# ['7/27/18,', '14:05', 'pablo']
	if (((afecto_individual[2]*100)/(len(cadena)-3) >= 25) or (count_bad_words*100/(len(cadena)-3) >= 20)):
		agresor_array.append(cadena[2])
	if ((afecto_individual[5]*100)/(len(cadena)-3) >= 25):
		victima_array.append(cadena[2])
	return total_words
#########################################################################
#	Se abre él .txt en una variable songarchivo
#	y se lee por lineas la canción desde songarchivo para luego
#	asignarla a una variable canción
def affect_processing():
	count_frases = 0
	with open("texto.txt") as archivo: # Abre el archivo en una variable nombrada "archivo"
		for frase in archivo: # recorre cada frase del archivo individualmente
			stop = [] # guarda los stopwords que deben eliminarse por cada frase
			frase = frase.lower() # deja toda la frase en minúsculas
			frase_split = frase.split() # divide la frase en palabras
			################################
			## Se remueven los stopwords
			for a in range(len(frase_split)): # recorre la frase palabra por palabra
				result = modulos.stopwords(frase_split[a]) # recibe un -1 si encuentra la palabra como stopword
				#print(result)
				if (result == -1):
					#print("se elimina la palabra %s" % frase_split[a])
					stop.append(frase_split[a]) # agrega el stopword al array "stop"
			for a in range(len(stop)):
				frase_split.remove(stop[a]) # remueve el stopword de la frase

			#print("%s: %s" % (frase_split, count_words(frase_split)))
			## Fin STOPWORDS
			################################
			## Inicio Stemming
			#frase_split = modulos.stem_tokens(frase_split, stemmer) # aplica stemming a las palabras restantes
			#print("STEAMMING APLICADO %s" % frase_split)
			## Fin Stemming
			################################
			#print(cadena)
			total_words = affect_analysis(frase_split) # indica a qué afecto corresponde cada palabra restante
			#print(afecto)
			count_frases = count_frases + 1

	print("count_frases: %s" % count_frases)
	#print (total_words)
	print("afecto: %s" % afecto)
	array3 = collections.Counter(agresor_array)
	array4 = collections.Counter(victima_array)
	agresor_detect = ''
	victima_detect = ''
	for letter in array3.most_common(1):
		agresor = list(letter)
		print("Posible agresor: %s" % agresor[0])
		agresor_detect = agresor[0]

	for letter in array4.most_common(1):
		victima = list(letter)
		print("Posible victima: %s" % victima[0][:-1])
		victima_detect = victima[0]

	print('cantidad frases: %s' % count_frases)
	print('cantidad de frases con prob de bullying: %s' % len(agresor_array))
	print('porcentaje de bullying: %s' % str(float(len(agresor_array)*100)/count_frases))
	return agresor_detect, victima_detect, float(len(agresor_array)*100)/count_frases
#########################################################################