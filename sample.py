# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 17:04:46 2022

@author: Ainun Nashwa
"""
#%%
from bs4 import BeautifulSoup
import requests

# Load Data
url = 'https://www.bac.edu.my/events/'
ext = 'iso'

# Extract the required informations
title=[] #List to store title of the website
desc=[] #List to store description of the website
image_url=[]#List to store image of the website
event_url=[]#List to store url of the event in the website
date=[] #List to store date of the website
time=[] #List to store start-date end-date of the website
  
domain = 'bac.edu.my/events/'
r = requests.post(url, {'domains': domain, 'submit': 'submit'})
soup = BeautifulSoup(r.content,'html.parser')

data = []

# Title
# print(soup.findAll("a", {"class": "mec-color-hover"}))
for item in soup.findAll("a", {"class": "mec-color-hover"}):   
    title.append(item.get_text())
    #   print(title, end="\n"*2)
    
# Description
for item in soup.findAll("div", {"class": "mec-event-description"}):
    desc.append(item.get_text())
    
# Image
for item in soup.findAll('img', class_='attachment-thumblist size-thumblist wp-post-image'):
    image_url.append(item['src'])
    
# Date
for item in soup.findAll("span", {"class": "mec-start-date-label"}):
    #date = item.get_text()
    date.append(item.get_text())   
    #print(date, end="\n"*2)
    
# Time
for item in soup.findAll("div", {"class": "mec-time-details"}):
    #time = item.get_text()
    time.append(item.get_text())
    #print(time, end="\n"*2)      

# URL
for item in soup.findAll("a", class_='mec-booking-button'):
    event_url.append(item['href'])

# List informations in the website
for i in range(len(title)):
    data.append({'Title': title[i],
                 'Description': desc[i],
                 'Image': image_url[i],
                 'URL' : event_url[i],
                 'Date': date[i],
                 'Time': time[i]})




    