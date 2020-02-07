# Links: https://www.udemy.com/course/web-scraping-python-tutorial/learn/lecture/12934390#overview
from bs4 import BeautifulSoup
import requests # Requests will allow you to send HTTP/1.1 requests using Python
import pandas as pd

url = "https://www.programmableweb.com/category/tools/api"

# url = 'https://www.programmableweb.com/category/all/apis?page=2050'

npo_API = {} # To save your data
API_no =  0 # Count how many jobs we already collected

while True: # continue collecting the data if it exists in the next page
	response = requests.get(url)
	print(response)

	# Check the connection to Website

	data = response.text
	# print(data)

	soup = BeautifulSoup(data,'html.parser') #offer an interface for programmers to easily access and modify the "HTML string code"
	# Link: find and findall in BeautifulSoup: http://www.programmersought.com/article/2030255808/
	# jobs = soup.find_all('div',{'class':'view-content'})
	jobs = soup.find_all('tbody')
	for job1 in jobs:
		for job in job1.find_all('tr'):
			API_Name_tag = job.find('td',{'class':'views-field views-field-title'})
			API_Name = API_Name_tag.text.strip() if API_Name_tag else 'N/A'
			API_Category_tag = job.find('td',{'class':'views-field views-field-field-article-primary-category'})
			API_Category = API_Category_tag.text.strip() if API_Category_tag else 'N/A'
			API_Version_tag = job.find('td', {'class': 'views-field views-field-pw-version-links'})
			API_Version = API_Version_tag.text.strip() if API_Version_tag else 'N/A'

			div = job.find('td', {'class': 'views-field views-field-title'})
			API_Link = 'https://www.programmableweb.com/' +  div.find('a')['href'] if div else 'N/A'# div.find('a')['href']
			# API_Link  = 'https://www.programmableweb.com/' + job.find('a').get('href')
			print('API Name:', API_Name, '\nAPI Category:', API_Category, '\nAPI Version:', API_Version, '\nAPI Link:', API_Link, '\n')

			API_no +=1
			npo_API[API_no]=[API_Name, API_Category,API_Version,API_Link ]
		# Check if butten next is on: we update url and continue collecting the data
	# li = soup.find('li', {'class': 'pager-last'}) # For link: https://www.programmableweb.com/category/all/apis
	# li = soup.find('li', {'class': 'pager-next'})
	a = soup.find('a',{'id':'pager_id_apis_all'})
	if a is None: # # len function to find the length of list
		break
	else:
		# url = 'https://www.programmableweb.com/' + li.find('a')['href']
		url = 'https://www.programmableweb.com/' + a.get('href')
# Export from dictionary in Python to cvx file
npo_API_df = pd.DataFrame.from_dict(npo_API, orient = 'index', columns =['API Name','Category','Version','Link'])

print(npo_API_df.head())

# Convert from data frame to csv file
npo_API_df.to_csv('npo_API.csv')
