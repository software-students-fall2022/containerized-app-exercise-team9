import requests

## function that gets the random quote
def get_random_quote():
	try:
		response = requests.get("https://api.quotable.io/random")
		if response.status_code == 200:
			json_data = response.json()
			return(json_data['content'])
		else:
			return "When nobody is around, the trees gossip about the people who have walked under them."
	except:
		print("Something went wrong.")
