from flask import Flask, request, render_template, render_template_string,url_for

app = Flask(__name__)


@app.route("/")
def hello():

	return render_template('index.html')


@app.route("/unsafe")
def unsafe_ssti():

	person = {'name': request.args.get('whoami'), 'secret': 'You win, master jedi!'}

	if person['name'] is None:
		person['name'] = 'world!'

	body = "Name: %s" % person['name']

	return render_template_string(body, person=person)

@app.route('/safe_ssti')
def safe_ssti():
	name = "world"
        template = 'this is safe: '
	if request.args.get('name'):
		name = request.args.get('name')
	return render_template_string(template, name=name)


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=80)
