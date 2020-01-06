from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from pprint import pprint
import pymongo
import datetime
import ssl
import config
import re
from pymongo import MongoClient

app = Flask(__name__)

# Connecting to MongoDB
# client = pymongo.MongoClient(config.MONGO_CLIENT_URL, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

# # Specifying the database
# db = client['email']

# # Regex for email validation
# regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

# # Function for validating email
# def check(email):
# 	if (re.search(regex, email)):
# 		return True
# 	else:
# 		return False

# # Flask routes
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return render_template('index.html')

# @app.route('/result', methods=['POST'])
# def subscribe():
# 	email = request.form['email']
# 	if not check(email):
# 		# Return render template
# 		return render_template('invalid-subscribe.html')
# 	collection = db['email']

# 	# Checks if email exists in the database and converts into boolean value
# 	email_exists = collection.find(
# 		{
# 			"email": email
# 		}
# 	).count() > 0

# 	if email_exists:
# 		return render_template('invalid-subscribe.html')
# 	else:
# 		post = {
# 			"email": email,
# 			"date": datetime.datetime.utcnow()
# 		}
# 		x = collection.insert_one(post).inserted_id
# 		print(x)

# 		# Return should render_template with like "Thank you for subscribing html page"
# 		return email

# @app.route('/unsubscribe', methods=['GET', 'POST'])
# def unsubscribe_home():
# 	return render_template('unsubscribe.html')

# @app.route('/unsubscribe/result', methods=['POST'])
# def unsubscribe():
# 	email = request.form['unsubscribe-email']
# 	collection = db['email']

# 	# Checks if email exists in the database and converts into boolean value
# 	email_exists = collection.find(
# 		{
# 			"email": email
# 		}
# 	).count() > 0
	
# 	if email_exists:
# 		delete = {
# 			"email": email
# 		}
# 		x = collection.delete_one(delete)
# 		print(x)
# 		# Return should render_template with like "unsubscribing html page"
# 		return email
# 	else:
# 		return render_template('invalid-unsubscribe.html')

@app.route('/', methods=['GET', 'POST'])
def home():
    return "please work"

if __name__ == '__main__':
   app.run()
