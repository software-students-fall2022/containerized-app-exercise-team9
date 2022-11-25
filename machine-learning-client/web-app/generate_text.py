import requests

## function that gets the random quote
def get_random_quote():
	try:
		response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
		if response.status_code == 200:
			json_data = response.json()
			data = json_data['data']
			return(data[0]['quoteText'])
		else:
			print("Error " + str(response.status_code) +  " while getting quote.")
	except:
		print("Something went wrong.")

get_random_quote()
