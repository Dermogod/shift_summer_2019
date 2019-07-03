from flask import Flask, request, render_template, render_template_string

app = Flask(__name__)


@app.route("/")
def hello():

	return render_template('index.html')


@app.route("/unsafe")
def unsafe_ssti():

	template = '''<title>No Injection Allowed!</title>
		<a href={{ url_for('hello_xss')}}?name={{ name |e}}>
		Click here for a welcome message</a>'''
	name = "world"
	if request.args.get('name'):
		name = request.args.get('name')
	return render_template_string(template, name=name)


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=80)
