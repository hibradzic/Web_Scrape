#!/usr/bin/env python
# coding: utf-8

# In[150]:


# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd


# In[2]:


# URL of page to be scraped
url= 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
# Retrieve page with the requests module
response = requests.get(url)


# In[3]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')


# In[4]:


# Extract title text
news_title = soup.title.text

# Print paragraph text
news_p = soup.body.p.text


# In[101]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

browser.click_link_by_partial_text('FULL IMAGE')


# In[105]:


browser.click_link_by_partial_text('more info')
response = requests.get(browser.url)

# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')

results = soup.find_all(attrs={"main_image"})
for result in results:
    featured_img = result.attrs['src']

featured_img = 'https://www.jpl.nasa.gov' + featured_img
featured_img


# In[47]:


# URL of page to be scraped
url= 'https://twitter.com/marswxreport?lang=en'
# Retrieve page with the requests module
response = requests.get(url)

# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')

results = soup.find_all('li', class_='js-stream-item stream-item stream-item ')
for result in results:
    firstTweet = result.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text

firstTweet


# In[151]:


# URL of page to be scraped
url= 'https://space-facts.com/mars/'
# Retrieve page with the requests module
response = requests.get(url)

# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')

tables = pd.read_html(url)
tables


# In[153]:


df = tables[0]
df.columns = ['Description', 'Data']
df.head()


# In[156]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
response = requests.get(browser.url)
headers = []

# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')

results = soup.find_all('h3')
for result in results:
    headers.append(result)

headers


# In[172]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
response = requests.get(browser.url)

# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')

results = soup.find_all('div', class_='downloads')

for result in results:
    featured_img = result.find('a')
    
first_img = featured_img.attrs['href']
first_img


# In[171]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
response = requests.get(browser.url)

# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')

results = soup.find_all('div', class_='downloads')

for result in results:
    featured_img = result.find('a')
    
second_img = featured_img.attrs['href']
second_img


# In[119]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
response = requests.get(browser.url)

# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')

results = soup.find_all('div', class_='downloads')

for result in results:
    featured_img = result.find('a')
    
third_img = featured_img.attrs['href']
third_img


# In[ ]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
response = requests.get(browser.url)

# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')

results = soup.find_all('div', class_='downloads')

for result in results:
    featured_img = result.find('a')
    
fourth_img = featured_img.attrs['href']
fourth_img


# In[173]:


hemisphere_image_urls = [
    {"title": headers[0], "img_url": first_img},
    {"title": headers[1], "img_url": second_img},
    {"title": headers[2], "img_url": third_img},
    {"title": headers[3], "img_url": fourth_img},
]
hemisphere_image_urls


# In[ ]:




