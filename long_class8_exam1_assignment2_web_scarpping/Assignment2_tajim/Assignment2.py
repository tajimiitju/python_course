
# coding: utf-8

# In[63]:


###Assignment 2 by Tajim
# topic:
# Scrape all data from this url "http://quotes.toscrape.com/"
# And dump the scrape data in a csv file.
# Column Header will be Quote, Author, Tags.
# All the tags will be in one cell and they will be separated by hifen "-"
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
scrape_url = 'http://quotes.toscrape.com/'
urlClnt = urlopen(scrape_url)
raw_html = urlClnt.read()
urlClnt.close()
page = soup(raw_html, 'html.parser')
#page
conteiners = page.findAll('div',{'class' : 'quote'})
#conteiners 
cont1 = conteiners[0]
#cont1
# Quote = cont1.find('span',{'class':'text'}).text
# Author= cont1.find('small',{'class':'author'}).text
# Tags = cont1.find('div',{'class':'tags'}).text.replace('\n','-').replace('-            Tags:-            -','')
# print(Quote)
# print(Author)
# print(Tags)

with open('assignment2_tajim.csv', 'w') as f:
    f.write('Quote, Author, Tags\n')
    for cont1 in conteiners:
        Quote = cont1.find('span',{'class':'text'}).text.replace(',','')
        Author= cont1.find('small',{'class':'author'}).text
        Tags = cont1.find('div',{'class':'tags'}).text.replace('\n','-').replace('-            Tags:-            -','')
#         print(Quote)
#         print(Author)
#         print(Tags)
        f.write(Quote+','+Author+','+Tags+'\n')

