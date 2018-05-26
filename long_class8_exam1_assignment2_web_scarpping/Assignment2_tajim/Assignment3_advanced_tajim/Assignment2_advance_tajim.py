
# coding: utf-8

# In[8]:


###Assignment 2 Advaced by Tajim
# topic:
# Scrape all data from this url "http://quotes.toscrape.com/"
# And dump the scrape data in a csv file.
# Column Header will be Quote, Author, Tags.
# All the tags will be in one cell and they will be separated by hifen "-"
# Advanced scarp all the 10 pages in 1 code
import sys
import codecs
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
base_url='http://quotes.toscrape.com/page/'
url_list1 = [10]
url_list1[0]='http://quotes.toscrape.com'
for i in range(2,11):
    url_list1.append("{}{}".format(base_url, str(i)))

#url_list1
with open('assignment2_Advance_tajim.csv', 'w') as f:
    f.write('Quote, Author, Tags\n')
    for i in range(0,10):
        urlClnt = urlopen(url_list1[i])
        raw_html = urlClnt.read()
        urlClnt.close()
        page = soup(raw_html, 'html.parser')
        conteiners = page.findAll('div',{'class' : 'quote'})
        cont1 = conteiners[0]
        for cont1 in conteiners:
            Quote = cont1.find('span',{'class':'text'}).text.replace(',','').replace('\u2032','')
            Author= cont1.find('small',{'class':'author'}).text.replace('\u2032','')
            Tags = cont1.find('div',{'class':'tags'}).text.replace('\n','-').replace('-            Tags:-            -','').replace('\u2032','')
            f.write(Quote+','+Author+','+Tags+'\n')
            #print(Quote+','+Author+','+Tags+'\n')

