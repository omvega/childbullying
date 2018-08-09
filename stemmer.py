import modulos
import os
import csv, operator
import nltk
from nltk import word_tokenize
from nltk.stem import SnowballStemmer

stemmer = nltk.SnowballStemmer('spanish')


with open("bad_words/bad_words.txt", 'r') as f:
	for line in f:
		#print(line)
		frase_split = line.split()
		frase_split = modulos.stem_tokens(frase_split, stemmer)
		print(frase_split[0])