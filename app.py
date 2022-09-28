from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
	#return render_template('register.html')
	return "Hello World"

"""
@app.route('/register',methods=["POST"])
def register():
	if request.method == 'POST':
		n = request.form.get('fname')
		return render_template('register.html',fname=n)
"""
