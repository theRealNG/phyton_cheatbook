# %% API Calls %%
import requests

# making a get request
headers = {"Authorization": "token 1f36137fbbe1602f779300dad26e4c1b7fbab631"}
response = requests.get("https://api.github.com/users/VikParuchuri", headers=headers)
response.json()

# making a post request
payload = {'name':'learning-about-apis'}
response = requests.post("https://api.github.com/user/repos", json=payload, headers=headers)

# making a patch request
payloads = {"description": "Learning about requests!", "name": "learning-about-apis"}
response = requests.patch("https://api.github.com/repos/VikParuchuri/learning-about-apis", json=payloads, headers=headers)

# making a delete request
response = requests.delete("https://api.github.com/repos/VikParuchuri/learning-about-apis", headers = headers)


# %% Scrapping %%
from bs4 import BeautifulSoup

response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
content = response.content

parser = BeautifulSoup(content, 'html.parser')

# get title text
title_text = parser.title.text

# find all p tags
body = parser.find_all("body")
p_all = body[0].find_all("p")
p1 = p_all[0].text

# find element by id
second_paragraph_text = parser.find_all("p", id="second")[0].text
second_text = parser.select("#second")[0].text

# find elements by class
second_inner_paragraph_text = parser.find_all("p","inner-text")[1].text
first_outer_text = parser.select(".outer-text")[0].text

patriots_total_plays_count = parser.select('#total-plays td')[2].text
