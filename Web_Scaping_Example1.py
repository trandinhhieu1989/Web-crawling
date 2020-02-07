# Link:https://www.glassdoor.com/Job/luxembourg-data-scientist-jobs-SRCH_IL.0,10_IN148_KO11,25.htm
# https://www.dataquest.io/blog/web-scraping-beautifulsoup/

from bs4 import BeautifulSoup
import requests # Requests will allow you to send HTTP/1.1 requests using Python
# from textblob import TextBlob

url = 'https://lu.indeed.com/Data-Scientist-jobs'

while True: # To search on the next page if it still has data to collect
	headers = {"Accept-Language": "en-US, en;q=0.5"} # https://www.dataquest.io/blog/web-scraping-beautifulsoup/
	response = requests.get(url,headers=headers)
	print(response)

	# data = response.text # Extracting text from the website
	# print(data)
	# soup = BeautifulSoup(data,'html.parser')

	# We need to imput the data to BeautifulSoup to allow BeautifulSoup to pass HTML tags with the help of html.parser
	soup = BeautifulSoup(response.text,'html.parser')
	# print(soup)

	# jobs = soup.find_all('div',{'class':'jobsearch-SerpJobCard unifiedRow row result clickcard'})
	jobs = soup.find_all('div',{'data-tn-component':'organicJob'})
	for job in jobs:
		# title = job.find('a')['title'] # https://stackoverflow.com/questions/43005780/how-to-obtain-title-attribute-using-python-and-beautifulsoup
		title = job.find('a',{'class':'jobtitle turnstileLink'}).get('title')
		company = job.find('span',{'class':'company'}).text.strip()
		location = job.find('span',{'class':'location accessible-contrast-color-location'}).text.strip()
		date = job.find('span', {'class':'date'}).text.strip()
		link_tag = job.find('a')['href']
		link = 'https://lu.indeed.com' + link_tag
		print('Job Title:',title,'\nCompany:',company,'\nLocation:',location,'\n Date:',date,'\n Link:',link,'\n')

		np
		url_tag = soup.find('a',{'title':'next page'})
		if url_tag.get('href'):
			url =
		# Using TextBlob to translate the output text from French to English
		# blob = TextBlob(date)
		# print(blob)
		# print(blob.detect_language())
		# date_en = blob.translate(to='en')
		# print(date_en)
		#
