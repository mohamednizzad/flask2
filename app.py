from flask import Flask,render_template,request

app = Flask(__name__)

if __name__ == "__main__":
	app.run(debug=True)

@app.route('/')
@app.route('/register')
def home():
	return render_template('register.html')

@app.route('/register',methods=['POST',"GET"])
def register():
	if request.method == 'POST':
		n = request.form.get('fname')
		return render_template('register.html',fname=n)