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


if __name__ == '__main__':
   app.run(debug=True)