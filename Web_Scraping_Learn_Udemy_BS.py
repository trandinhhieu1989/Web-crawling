# Links: https://www.udemy.com/course/web-scraping-python-tutorial/learn/lecture/12934390#overview
from bs4 import BeautifulSoup
import requests # Requests will allow you to send HTTP/1.1 requests using Python
import pandas as pd

url = "https://boston.craigslist.org/search/sof"

# # Create a dictionary
# d = {'key':'value'}
# print(d)
#
# # Update the dictionary
# d['new key'] = 'new value'
# print(d)

npo_jobs = {} # To save your data
job_no =  0 # Count how many jobs we already collected

while True: # continue collecting the data if it exists in the next page
	response = requests.get(url)
	print(response)

	# Check the connection to Website

	data = response.text
	# print(data)

	soup = BeautifulSoup(data,'html.parser') #offer an interface for programmers to easily access and modify the "HTML string code"

	# # 1. Find jobs and addresses of those jobs separately
	# tags = soup.find_all('a') # or soup_findAll('a')
	#
	# # for tag in tags:
	# # 	print(tag.get('href'))
	#
	# titles = soup.find_all('a',{'class':'result-title'}) # or class_='result-title'
	#
	# for title in titles:
	# 	print(title.text)
	#
	# addresses = soup.find_all('span', class_='result-hood')
	# for address in addresses:
	# 	print(address.text)

	# 2. Find Jobs associated with addresses.
	# Link: find and findall in BeautifulSoup: http://www.programmersought.com/article/2030255808/
	jobs = soup.find_all('p',{'class':'result-info'})
	for job in jobs:
		title = job.find('a',{'class':'result-title hdrlnk'}).text
		location_tag = job.find('span',{'class':'result-hood'})
		location = location_tag.text[2:-1].strip() if location_tag else 'N/A' # get_text().strip() get_text(strip=True) strip to remove the extra spaces
		# since we know exactly the structure of the text in location, i.e., space(text). Thus, we can use text[2:-1] to
		# remove the brackets () https://www.w3schools.com/python/showpython.asp?filename=demo_string_negativeindex
		# https://www.w3schools.com/python/showpython.asp?filename=demo_string2
		date = job.find('time',{'class':'result-date'}).text
		link = job.find_all('div',{'class':'result-title'}).get('href')

		job_no +=1
		npo_jobs[job_no]=[title, location,date,link]
		# print(npo_jobs)
		#
		# print('Job Title:', title, '\nLocation of Jobs', location, '\nDate Started', date, '\nLink', link, '\n')

		# # Print out the description in that job
		# job_response = requests.get(link)
		# job_data = job_response.text
		# job_soup = BeautifulSoup(job_data,'html.parser') # Input to BeautifulSoup
		#
		# # print what we want now
		# job_attribute_tag = job_soup.find('p', {'class': 'attrgroup'})
		# job_attribute = job_attribute_tag.text if job_attribute_tag else 'N/A'
		# job_description = job_soup.find('section',{'id':'postingbody'}).text.strip()
		#
		# print('Job Title:', title,'\nLocation',location,'\nDate',date,'\nLink',link,'\n',
		#       job_attribute,'\nJob Description:',job_description,'\n')

		# Check if butten next is on: we update url and continue collecting the data
	url_tag = soup.find('a', {'title': 'next page'})
	if url_tag.get('href'):
		url = 'https://boston.craigslist.org'+ url_tag.get('href')
			# print(url)
	else:
		break

# Export from dictionary in Python to cvx file
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.from_dict.html
# Specify orient='index' to create the DataFrame using dictionary keys as rows:
#  the column names can be specified manually: columns['A','B']
npo_jobs_df = pd.DataFrame.from_dict(npo_jobs, orient = 'index', columns =['Job Title','Location','Posted Date','Link'])

print(npo_jobs_df.head())

# Convert from data frame to csv file
npo_jobs_df.to_csv('npo_job.csv')
