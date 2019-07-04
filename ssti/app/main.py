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
	client_data=request.get_data('whoami')
	return render_template_string('thisisafe', client_data=client_data)


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=80)
