from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from pprint import pprint
import pymongo
import datetime
import ssl
import config
from pymongo import MongoClient


app = Flask(__name__)

client = pymongo.MongoClient(config.MONGO_CLIENT_URL, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
db = client['email']

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def subscribe():
	email = request.form['email']
	print(email)
	collection = db['email']
	post = {
		"email": email,
		"date": datetime.datetime.utcnow()
	}
	x = collection.insert_one(post).inserted_id
	print(x)

	# Return should render_template with like "Thank you for subscribing html page"
	return email

@app.route('/unsubscribe', methods=['GET', 'POST'])
def unsubscribe_home():
	return render_template('unsubscribe.html')

@app.route('/unsubscribe/result', methods=['POST'])
def unsubscribe():
	email = request.form['unsubscribe-email']
	collection = db['email']

	# Checks if email exists in the database and converts into boolean value
	email_exists = collection.find(
		{
			"email": email
		}
	).count() > 0
	
	if email_exists:
		delete = {
			"email": email
		}
		x = collection.delete_one(delete)
		print(x)
		# Return should render_template with like "unsubscribing html page"
		return email
	else:
		print("Email does not exist in the database")
		return ("Email doesn't exist.")

if __name__ == '__main__':
   app.run(debug=True)