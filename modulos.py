import csv, operator
import nltk
from nltk.stem import SnowballStemmer
stemmer = nltk.SnowballStemmer('spanish')

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

#	método para buscar en qué afecto o si se encuentra 
#	la palabra, si la encuentra retorna un -2	
#
"""def affect (palabra, afectocsv):
	#abre el csv
	csvarchivo = open(afectocsv) #abre el csv
	entrada = csv.reader(csvarchivo) #asigna los elementos del archivo a una variable
	#se recorre el csv hasta encontrar la palabra
	for c in entrada:
		#afectoff = c
		
		#afectoff = stem_tokens(afectoff, stemmer)
		if (c[0] == palabra):
			#print ("ENTRÓ AL CICLO")
			#print (palabra)		
			#print(afectoff)	
			#print(afectocsv)
			return -2
	csvarchivo.close()"""

def affect (palabra, afectocsv):
	if palabra in open(afectocsv).read():
		return -2

"""def affect (palabra, afectocsv):
	with open(afectocsv, 'r') as f:
		for line in f:
			#print(line)
			if palabra in line:
				return -2"""
############################################################
#	método que elimina los stopWords
#	devuelve un -1 cuando encuentra una palabra que no 
#	tiene incidencia en los afectos
"""def stopwords (palabra):
	archivo = open('stopwords.csv')
	linea = csv.reader(archivo)
	#print (linea)
	for y in linea:
		#print ("Se analiza la palabra: %s" % y)
		if (y[0] == palabra):
			###	Descomentar para ver los
			###	stopword que se sacan del texto
			#print ("Se remueve la palabra: %s" % y[0])
			return -1
	archivo.close()"""
"""
def stopwords (frase):
	with open("stopwords.txt", 'r') as f:
		for line in f:
			if frase+'\n' == line:
				print("SE ENCONTRÓ")
				return -1"""

def stopwords (frase):
	if frase in open('stopwords.txt').read():
		return -1

def bad_words (word):
	#if word == open('bad_words/bad_words_stemmer.txt').read():
	#	return -1

	with open("bad_words/bad_words.txt", "r") as archivo_palabras:
	    contenido = archivo_palabras.read()
	    contenido = contenido.split()
	    for badword in contenido:
	    	if badword == word:
	    		return -1
############################################################
def cancion (palabra):
	songarchivo = open("cancion.txt")
	cancion = songarchivo.readlines()
	for can in cancion:
		if(can == palabra):
			print("se encontró la palabra")
############################################################