from flask import Flask
from flask import render_template
import forms
from flask import request, redirect
import affect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	text_form = forms.TextForm(request.form)
	nombre = 'Usuario'
	#si pasa el "if" muestra resultado, sino vuelve a cargar la plantilla
	if request.method == 'POST' and text_form.texto.data != '': #que sea POST y que el TextArea no esté vacio
		print (text_form.texto.data)
		archivo = open('cancion.txt', 'w+')
		archivo.write(text_form.texto.data)
		archivo.close()
		agresor, victima, porcentaje = affect.affect_processing('cancion.txt')
		return render_template('resultado.html', 	name = nombre, 
													agresor = agresor, 
													victima = victima,
													porcentaje = porcentaje)
	else:
		return render_template ('index.html', text=text_form)



@app.route('/resultado')
def  resultado():
	return render_template ('resultado.html')



if __name__ == '__main__':
	app.run(debug = True, port=8000)