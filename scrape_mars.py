
# coding: utf-8

# In[1]:


# Dependencies
import pandas as pd
import re
import requests
import pymongo
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver   


# In[2]:


# Scrape the NASA Mars News Site and collect the latest News Title and Paragragh Text
# Assign the text to variables that you can reference later


# In[3]:


path = {'executable_path': './Untitled Folder/chromedriver.exe'}


# In[4]:


# Obtain html of Mars website
mars_news_url = 'https://mars.nasa.gov/news/'
mars_news_html = requests.get(mars_news_url)


# In[5]:


# Parse html file with BeautifulSoup# Parse 
mars_soup = BeautifulSoup(mars_news_html.text, 'html.parser')


# In[6]:


# Print body of html
print(mars_soup.body.prettify())


# In[7]:


# Find article titles
article_titles = mars_soup.find_all('div', class_='content_title')
article_titles


# In[8]:


# Loop to get article titles# Loop  
for article in article_titles:
    title = article.find('a')
    title_text = title.text
    print(title_text)


# In[9]:


paragraphs = mars_soup.find_all('div', class_='rollover_description')
paragraphs


# In[10]:


# Loop through paragraph texts
for paragraph in paragraphs:
    p_text = paragraph.find('div')
    news_p = p_text.text
    print(news_p)


# In[11]:


# Open browser of Mars space images

#revisit this
#mars_images_browser = Browser('chrome', headless=False)

mars_images_browser = Browser('chrome', **path)

nasa_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
mars_images_browser.visit(nasa_url)


# In[12]:


# Parse html file with BeautifulSoup
mars_images_html = mars_images_browser.html
nasa_soup = BeautifulSoup(mars_images_html, 'html.parser')


# In[13]:


# Print body of html
print(nasa_soup.body.prettify())


# In[14]:


# Find image link with BeautifulSoup
images = nasa_soup.find_all('div', class_='carousel_items')
images


# In[15]:


# Loop through images
for nasa_image in images:
    image = nasa_image.find('article')
    background_image = image.get('style')
    # print(background_image)
    
  
    re_background_image = re.search("'(.+?)'", background_image)
    # print(re_background_image)
    
    # Convert match object (url link) to string
    # group(0) includes quotations
    # group(1) gets the url link
    search_background_image = re_background_image.group(1)
    # print(search_background_image)
    
    featured_image_url = f'https://www.jpl.nasa/gov{search_background_image}'
    print(featured_image_url)


# In[16]:


# Get weather tweets with splinter
path = {'executable_path': './Untitled Folder/chromedriver.exe'}
twitter_browser = Browser('chrome', **path)
twitter_url = 'https://twitter.com/marswxreport?lang=en'
twitter_browser.visit(twitter_url)


# In[17]:


# Parse html file with BeautifulSoup
twitter_html = twitter_browser.html
twitter_soup = BeautifulSoup(twitter_html, 'html.parser')


# In[18]:


# Print body 
print(twitter_soup.body.prettify())


# In[19]:


# Find weather tweets with BeautifulSoup
mars_weather_tweets = twitter_soup.find_all('p', class_='TweetTextSize')
mars_weather_tweets


# In[20]:


# Get tweets that begin with 'Sol' which indicate weather
weather_text = 'Sol '

for tweet in mars_weather_tweets:
    if weather_text in tweet.text:
        mars_weather = tweet.text
        print(tweet.text)


# In[21]:


#Mars Facts


# In[22]:


# Url to Mars facts website
mars_facts_url = 'https://space-facts.com/mars/'
mars_fact_table = pd.read_html(mars_facts_url)
mars_fact_table


# In[23]:


mars_fact = mars_fact_table[0]

# Switch columns and rows
mars_fact_df = mars_fact.transpose()
mars_fact_df


# In[24]:


# Rename columns
mars_fact_df.columns = [
    'Equatorial diameter',
    'Polar diameter',
    'Mass',
    'Moons',
    'Orbit distance',
    'Orbit period',
    'Surface temperature',
    'First record',
    'Recorded by'
]

mars_fact_df


# In[25]:


c_mars_facts_df = mars_fact_df.iloc[1:]
c_mars_facts_df


# In[26]:


# Print dataframe in html format
mars_facts_html_table = c_mars_facts_df.to_html()
print(mars_facts_html_table)


# In[27]:


# Mars Hemispheres
# Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres


# In[28]:


path = {'executable_path': './Untitled Folder/chromedriver.exe'}
usgs_browser = Browser('chrome', **path)
usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
usgs_browser.visit(usgs_url)


# In[29]:


mars_hemispheres_html = usgs_browser.html
mars_hemispheres_soup = BeautifulSoup(mars_hemispheres_html, 'html.parser')


# In[30]:


print(mars_hemispheres_soup.body.prettify())


# In[31]:


# Find hemisphere image link and title
mars_hemispheres = mars_hemispheres_soup.find_all('div', class_='description')
mars_hemispheres

