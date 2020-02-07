# Link: https://www.youtube.com/feed/trending
# In this code, we try to scape top trending videos on Youtube to cache at the mobile edge

from bs4 import BeautifulSoup
import requests # Requests will allow you to send HTTP/1.1 requests using Python

url = 'https://www.youtube.com/feed/trending'
headers = {"Accept-Language": "en-US, en;q=0.5"}
# response = requests.get(url, headers).text
response = requests.get(url, headers)
print(response) # Check the response from the website

soup = BeautifulSoup(response.text, 'html.parser')
# jobs = soup.find_all('div',{'id':'dismissable'})
jobs = soup.find_all('ytd-video-renderer',{'class':'style-scope ytd-expanded-shelf-contents-renderer'})

for job in jobs:
	title = job.find('a',{'id':'video-title'}).get('title')
	# print('Title of Youtube trending videos:',title)
	print(title)

