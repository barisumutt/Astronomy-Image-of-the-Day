import streamlit as st
import requests


# Get image from the website
image_url = "https://apod.nasa.gov/apod/image/2305/EagleDeep_Lacroce_1080.jpg"
response = requests.get(image_url)

with open("images/image.jpg", "wb") as file:
    file.write(response.content)

# Get information from the website
api_key = "zEFBwm5W28FMe4CYcT3Ci5fBPZnAifKPrMLgx3fB"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

#Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the title
title_body = ""
for title in content["title"]:
      title_body = title_body + title

# Access the description
description_body = ""
for description in content["description"]:
      description_body = description_body + description




