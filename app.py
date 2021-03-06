from flask import Flask, render_template, request, url_for, session, redirect
import giphy #GIPHY api
from utils import getEmotion

app= Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html", 	gif1 = giphy.getURL("")[0],
											gif2 = giphy.getURL("")[1],
											gif3 = giphy.getURL("")[2],
											gif4 = giphy.getURL("")[3],
											gif5 = giphy.getURL("")[4],
											gif6 = giphy.getURL("")[5],
											gif7 = giphy.getURL("")[6],
											gif8 = giphy.getURL("")[7],
											gif9 = giphy.getURL("")[8],
											gif10 = giphy.getURL("")[9],
											)

@app.route("/results", methods =['POST','GET'])
def results():
	if request.method == 'POST':
		#rint request.form
		if 'input' in request.form:
			text = request.form['input']
	lyric = getEmotion.getMatch(text)
	print lyric + "hi"
	return render_template("index.html", 	lyric = lyric,
											gif1 = giphy.getURL(text)[0],
											gif2 = giphy.getURL(text)[1],
											gif3 = giphy.getURL(text)[2],
											gif4 = giphy.getURL(text)[3],
											gif5 = giphy.getURL(text)[4],
											gif6 = giphy.getURL(text)[5],
											gif7 = giphy.getURL(text)[6],
											gif8 = giphy.getURL(text)[7],
											gif9 = giphy.getURL(text)[8],
											gif10 = giphy.getURL(text)[9],)

if __name__ == "__main__":
	app.debug = True
	app.run()
