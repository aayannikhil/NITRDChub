# from urllib2.request import urlopen
# from bs4 import BeautifulSoup as soup
#
# myurl = 'https://ngupta.me/'
#
# #opening the connection, grabbing the page
# uClient = urlopen(myurl)
# page_html = uClient.read()
# uClient.close()

# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://ngupta.me'

# query the website and return the html to the variable ‘page’
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, ‘html.parser’)

# Take out the <div> of name and get its value
name_box = soup.find(‘h3’, attrs={‘id’: ‘about’})

print name_box
