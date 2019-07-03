from flask import Flask, request, render_template, render_template_string

app = Flask(__name__)


@app.route("/")
def hello():

	return render_template('index.html')


@app.route("/unsafe")
def unsafe_ssti():

	person = {'name': request.args.get('whoami'), 'secret': 'You win, master jedi!'}

	body = '''<title>No Injection Allowed!</title>
                <a href={{ url_for('hello_xss')}}?person={{person |e}}>
                Click here for a welcome message</a>'''
        
        if person['name'] is None:
            person['name']='world!'

	return render_template_string(body, person=person)


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=80)
