##
## scrapes the clark county contracts website and writes to a text file. basis of www.portlandvancouverwatchdog.com
##

## import beautifulsoup for scraping, urllib2 for opening webpages
from bs4 import BeautifulSoup
import urllib2

## url of clark county contracts website
r = urllib2.Request('http://www.clark.wa.gov/contracts-grid/')
## make a handler to use with spoofer
opener = urllib2.build_opener()
## spoof browser user agent so the website doesn't think we are a bot
r.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0')
## have handler open website with spoofed user agent and read website
contracts = opener.open(r).read()
## run output into beautifulsoup 
soup = BeautifulSoup(contracts)
## find locations of contract info and contract pdfs
contract = soup.find_all("td", class_="views-field views-field-field-local-fund-amount")
contract1 = soup.find_all("td", class_="views-field views-field-body-1")
## write to text file
text_file = open('clark county contracts.txt', 'a')

## uses a for loop to grab, save and print pdf file url, uses another for loop on info about contract


for x in contract1:
    thing = 'https://www.clark.wa.gov' + x.a['href'] + ' \n'
    print thing
    text_file.write(thing.encode('utf-8'))


for x in contract:
    thing = x.get_text('\t')
    print thing
    text_file.write(thing.encode('utf-8'))

