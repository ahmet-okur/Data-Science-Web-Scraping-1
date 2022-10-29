#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import required libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen


# In[2]:


#url for web scraping
url = 'http://www.simplilearn.com/resources'


# In[3]:


#scrape the web page document
webpage = urlopen(url)


# In[4]:


#create the soup object and parse the webpage using html.parser
sl_soup = BeautifulSoup(webpage,'html.parser')


# In[5]:


#close the webpage object
webpage.close()


# In[6]:


#view the soup contents
sl_soup.contents


# In[7]:


#use pretiffy method to view the well formatted html output
print (sl_soup.prettify())


# In[8]:


#view the title of the scraped document
sl_soup.title


# In[9]:


#find all herf link present the web page
for href in sl_soup.findAll('a',href=True):
    print (href['href'])


# In[10]:


#View all the headers name
#the div information is obtained from the web page (view page source)
for article in sl_soup.find_all('h2'):
    print (article.string)


# In[11]:


#View all the resource topics
#the class information is obtained from the web page (view page source)
for article_topic in sl_soup.find_all('h4'):
    print (article_topic.string)


# In[12]:


#create article object for finding the list
#the class information is obtained from the web page (view page source)
url2 = "https://www.simplilearn.com/scrum-master-roles-responsibilities-qualities-article?souce=frs_home"
webpage2 = urlopen(url2)
s1_article = BeautifulSoup(webpage2, "html.parser")
article_name = s1_article.find(class_ = "desig_author empty-text")


# In[13]:


#view the type of the article object
type(article_name)


# In[14]:


#find all the article names
article_name.findAll('p')


# In[15]:


#find first article name
find_first_article = article_name.p
print(find_first_article.prettify())


# In[16]:


#find next sibling (next article name)
find_next_article = find_first_article.next_sibling.next_sibling
find_next_article


# In[17]:


#find previous sibling (previous article name)
find_previous_article = find_next_article.previous_sibling.previous_sibling
find_previous_article


# In[ ]:




