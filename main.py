import requests

api_key = "65f5c447242040e8b9a5a5ac77678a9d"
url = "https://newsapi.org/v2/top-headlines?country=us" \
      "&category=business&apiKey=" \
      "65f5c447242040e8b9a5a5ac77678a9d"
# Make request
request = requests.get(url)
# Get a dictionary with the data
content = request.json()
# Print title and content of each article
for article in content["articles"]:
    print(article["title"])
    print(article["description"])