from flask import Flask, request, render_template, render_template_string

app = Flask(__name__)


@app.route("/")
def hello():

	return render_template('index.html')


@app.route("/unsafe")
def unsafe_ssti():

	person = {'name': request.args.get('whoami'), 'secret': 'You win, master jedi!'}
	if person['name'] is None:
		person['name'] = 'world!'
	body =  " Nameee: %s " % person['name']
	blacklist = ["__class__{{}}.()"]
        for bad_string in blacklist:
                if  bad_string in person.name:
                return "HACK ATTEMPT {}".format(bad_string), 400

	return render_template_string( body, person=person)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=80)
