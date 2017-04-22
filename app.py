from flask import Flask, render_template, request, url_for, session, redirect
from utils import search
from utils import rake
#from utils import translator

app= Flask(__name__)

@app.route("/")
@app.route("/home/", methods = ['POST', 'GET'])
def home():
	if request.method == 'GET':
		return render_template('index.html', ID = "")
	else:
		search_term = request.form['lyric']
		outputfilename = search.setup(search_term)
		client_id, client_secret, client_access_token = search.load_credentials()
		return render_template('index.html', ID= search.search(request.form['lyric'],rake.do(search_term),outputfilename,client_access_token))#, hi=translator.prep(search.setup(search_term)))


if __name__ == "__main__": 
	app.debug = True
	app.run() 