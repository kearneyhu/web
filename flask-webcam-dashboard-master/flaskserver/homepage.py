from flask import (
	Flask,
	g,
	redirect,
	render_template,
	request,
	session,
	url_for
)
from sense_hat import SenseHat
import time
import pictures as images
import os

class User:
	def __init__(self, id, username, password):
		self.id = id
		self.username = username
		self.password = password

users = []
users.append(User(id=1, username='admin', password='password'))
users.append(User(id=2, username='tester', password='testpassword'))

app = Flask(__name__)
app.secret_key = 'ELEC5518-Group8-Ivan-Kearney-Garson'

sense = SenseHat()

@app.before_request
def before_request():
	g.user = None

	if 'user_id' in session:
		search_results = [x for x in users if x.id == session['user_id']]
		if len(search_results) != 0:
			user = search_results[0]
			g.user = user

@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET','POST'])
def login():
	os.system("sudo service motion stop")

	if request.method == 'POST':
		session.pop('user_id', None)

		username = request.form['username']
		password = request.form['password']

		search_results = [x for x in users if x.username == username]
		if len(search_results) != 0:
			user = search_results[0]
			if user and user.password == password:
				session['user_id'] = user.id
				return redirect(url_for('lock'))

		return redirect(url_for('login'))

	return render_template('login.html')



@app.route("/locked")
def lock():
	os.system("sudo service motion stop")

	if not g.user:
		return redirect(url_for('login'))

	sense.set_pixels(images.lock_image)
	return render_template('locked.html')

@app.route("/webcamon")
def webcamon():
	os.system("sudo service motion start")
	time.sleep(4)

	if not g.user:
		return redirect(url_for('login'))

	sense.set_pixels(images.lock_image_recording)
	return render_template('webcamon.html')

@app.route("/unlocked")
def unlock():
	if not g.user:
		return redirect(url_for('login'))

	sense.set_pixels(images.unlock_image_recording)
	return render_template('unlock.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
