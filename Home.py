import streamlit as st
import requests


# Download the image
image_url = "https://apod.nasa.gov/apod/image/2305/EagleDeep_Lacroce_1080.jpg"
response = requests.get(image_url)

with open("images/image.jpg", "wb") as file:
    file.write(response.content)

# Prepare API key and API url
api_key = "zEFBwm5W28FMe4CYcT3Ci5fBPZnAifKPrMLgx3fB"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

# Get the request data as a dictionay
request = requests.get(url)
data = request.json()

# Extract the title
title = data["title"]

# Extract the explanation
explanation = data["explanation"]

# Set the page
st.set_page_config(layout="wide")

st.title(f"{title}")
st.image("images/image.jpg")
st.write(f"{explanation}")


