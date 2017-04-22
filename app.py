from flask import Flask, render_template, request, url_for, session, redirect
from utils import search
from utils import rake
#from utils import translator

app= Flask(__name__)

@app.route("/")
def home():
	return render_template(index.html)

if __name__ == "__main__":
	app.debug = True
	app.run()
