import requests
import os
from send_email import send_email

api_key = "65f5c447242040e8b9a5a5ac77678a9d"
url = "https://newsapi.org/v2/top-headlines?country=us" \
      "&category=business" \
      "&apiKey=65f5c447242040e8b9a5a5ac77678a9d" \
      "&language=en"
# Make request
request = requests.get(url)

# Get a dictionary with the data
content = request.json()

# Print title and content of each article
raw_message = ""
for article in content["articles"][0:20]:
    raw_message = f"{raw_message}\n\n{article['title']}\n{article['description']}\n{article['url']}"

message = f"""\
Subject: Today's News

{raw_message}
"""
send_email(message.encode("utf-8"))

