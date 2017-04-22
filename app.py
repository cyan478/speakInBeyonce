from flask import Flask, render_template, request, url_for, session, redirect
#from utils import search
#from utils import rake
#from utils import translator

#----------------- GIPHY API ----------------- 
import urllib,json
data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=beyonce&api_key=dc6zaTOxFJmzC&limit=5").read())
#print json.dumps(data, sort_keys=True, indent=4)

def getURL():
	d = data["data"]
	ret = []
	for gif in d:
		ret.append(gif['images']['downsized']['url'])
	return ret
#----------------- GIPHY API end ----------------- 

app= Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html", 	gif1 = getURL()[0],
											gif2 = getURL()[1],
											gif3 = getURL()[2],
											gif4 = getURL()[3],
											gif5 = getURL()[4],)

if __name__ == "__main__":
	app.debug = True
	app.run()
