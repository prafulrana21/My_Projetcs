from flask import Flask, render_template, flash, request,session
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from getdp.img import getimg
from flask_bootstrap import Bootstrap
from PIL import Image
from io import BytesIO
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
import requests
# App config.
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(FlaskForm):
	username = StringField("Enter Instagram User name",validators=[DataRequired()])
	submit=SubmitField('Submit')
@app.route("/", methods=['GET', 'POST'])
def hello():
	img=''
	form = ReusableForm()
	if form.validate_on_submit():
		session['username']=form.username.data
		img=getimg.calling(session['username'])
		#return render_template('hello1.html',img=img)
	return render_template('hello1.html', form=form,img=img)
if __name__ == "__main__":
	app.run(debug=True)