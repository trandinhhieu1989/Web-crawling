# -*- coding: utf-8 -*-
# from time import sleep
#
# from scrapy import Spider
# from selenium import webdriver
# from scrapy.selector import Selector
# from scrapy.http import Request
# from selenium.common.exceptions import NoSuchElementException

import json
# import scrapy
from scrapy import Spider
import objectpath

from scrapy import Request

from time import sleep
from scrapy.selector import Selector


import urllib.request

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# import random



class BentleyCrawlSpider(Spider):
    name = 'Bentley_crawl'
    allowed_domains = ['bentley.wd1.myworkdayjobs.com']
    start_urls = ['https://bentley.wd1.myworkdayjobs.com/en-US/faculty/job/Bentley-Campus']

    def parse(self,response):
        # with open('web.json', 'r') as f: # open a json file
        #     # content = f.readlines()
        #     # for i in content:
        #     #     if "commandLink" in i:
        #     #         print(i)
        #     data = json.load(f)
        url = 'https://bentley.wd1.myworkdayjobs.com/faculty'
        req = urllib.request.Request(url)
        req.add_header('Accept', 'application/json,application/xml')
        a = urllib.request.urlopen(req).read().decode('utf-8')
        sleep(3)
        data = json.loads(a)
        # print(data)

        jsonnn_tree = objectpath.Tree(data['body'])
        result_tuple = tuple(jsonnn_tree.execute('$..commandLink'))
        for i in result_tuple:
            # print(i,'\n')
            url = 'https://bentley.wd1.myworkdayjobs.com' + i
            print(url,'\n')
            # Extract data from html from website url
            driver = webdriver.Chrome(r'C:\Users\hieu.tran-dinh\Desktop\python_code\Web_Scraping\chromedriver')
            sleep(3)
            driver.get(url)
            sleep(3)
            yield Request(url, callback=self.parse_jobs)

            # # Using Json file to extract the data from url
            # req = urllib.request.Request(url) # https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.add_header
            # req.add_header('Accept', 'application/json,application/xml') # Example 1 https://www.programcreek.com/python/example/73735/urllib.request.add_header
            # a = urllib.request.urlopen(req).read().decode('utf-8') # Example 10
            # sleep(2)
            # data = json.loads(a)
            # # print(data)
            # jsonnn_tree = objectpath.Tree(data['openGraphAttributes'])
            # title = tuple(jsonnn_tree.execute('$..title'))
            # Job_Description = tuple(jsonnn_tree.execute('$..description'))
            # # print(title)
            # # print(Job_Description)
            # yield{'title': title, 'Job Description':Job_Description,'Url':url}

    def parse_jobs(self, response):
        sleep(5)
        for sel in response.xpath('//div[@class="WGEP WBDP WDFP WI5 wd-ViewPage"]'):
            title = sel.xpath('//h1/text()').extract_first()
            print(title)
            yield {'title': title}





#     def parse(self, response):
#         quotes = response.xpath('//div[@class="quote"]')
#         for quote in quotes:
#             text = quote.xpath('.//*[@itemprop="text"]/text()').extract_first("")[1:-1].strip()
#             author = quote.xpath('.//*[@itemprop="author"]/text()').extract_first()
#             tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()
#
#             yield {'Text': text, 'Author': author, 'Tags': tags}
#             print('Text', text, '\nAuthor', author, '\nTags', tags, '\n')
#         next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
#         absolute_next_page_url = response.urljoin(next_page_url)'
#         # absolute_next_page_url = "http://quotes.toscrape.com" + next_page_url
#         yield Request(absolute_next_page_url, callback=self.parse)
#
#
# sleep(random.randrange(1, 3))



    # def start_requests(self):
    #     self.driver = webdriver.Chrome(r'C:\Users\hieu.tran-dinh\Desktop\python_code\Web_Scraping\chromedriver')
    #     self.driver.get('https://bentley.wd1.myworkdayjobs.com/faculty')
    #     # sleep(4)
    #     # assigning the source code for the web page to variable sel
    #     sel = Selector(text=self.driver.page_source)
    #     # Find the information of all jobs
    #     jobs = sel.xpath('//div[@class="WD3O WO1O WI2O"]').extract_first()
    #     # jobs = self.driver.find_element_by_xpath('//div[@class="WD3O WO1O WI2O"]')
    #     for job in jobs:
    #         try:
    #             next_page =  self.driver.find_element_by_xpath('//div[@class="gwt-Label WE3O WO1O"]')
    #             # next_page = job.click()
    #             sleep(3)
    #             self.logger.info('Sleeping for 3 seconds.')
    #             next_page.click()
    #
    #             new_page = Selector(text=self.driver.page_source)
    #             title = new_page .xpath('.//div[@class="GWTCKEditor-Disabled"]/h1/text()').extract_first()
    #             yield{'Title':title}
    #             print(title)
    #
    #         except NoSuchElementException:
    #             self.logger.info('No more pages to load.')
    #             self.driver.quit()
    #             break

    # def parse_book(self, response):
    #     pass
