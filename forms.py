# install forms-wtf

from wtforms import Form
from wtforms import TextAreaField

class TextForm(Form):
	texto = TextAreaField()