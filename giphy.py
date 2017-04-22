import urllib,json

def getURL( UI ):
	front = "http://api.giphy.com/v1/gifs/search?q="
	userInput = UI
	end = "+beyonce&api_key=dc6zaTOxFJmzC&limit=10"
	searchURL = front + userInput + end

	data = json.loads(urllib.urlopen( searchURL ).read())
	#print json.dumps(data, sort_keys=True, indent=4)

	d = data["data"]
	ret = []
	for gif in d:
		ret.append(gif['images']['downsized']['url'])
	return ret