from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient


# Try figure out the databases
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/randoggo"
mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def subscribe():
	email = request.form['email']
	print(email)

	# Return should render_template
	return email



if __name__ == '__main__':
   app.run(debug=True)