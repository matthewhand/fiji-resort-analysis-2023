
import os
import requests

# Get the RapidAPI key from the environment variables
RAPIDAPI_API_KEY = os.getenv('RAPIDAPI_API_KEY')

# Define the headers for the RapidAPI requests
headers = {
    'x-rapidapi-key': RAPIDAPI_API_KEY,
    'x-rapidapi-host': 'hotels4.p.rapidapi.com'
}

# Define the URL for the Hotels4 API request
url = 'https://hotels4.p.rapidapi.com/locations/search'

# Define the query string parameters for the Hotels4 API request
querystring = {'query':'Beqa Lagoon'}

# Make the GET request to the Hotels4 API
response = requests.request('GET', url, headers=headers, params=querystring)

# Get the JSON data from the response
data = response.json()

# Process the data and format it for the research file
content = ''
for suggestion in data['suggestions'][0]['entities']:
    content += f"## {suggestion['name']}
"
    content += f"Type: {suggestion['type']}
"
    content += f"Score: {suggestion['score']}
"
    content += '
'
