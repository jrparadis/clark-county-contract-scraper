##
## scrapes the clark county contracts website and writes to a text file.
##

## import beautifulsoup for scraping, urllib2 for opening webpages
from bs4 import BeautifulSoup
import urllib2
import ftplib




## url of clark county contracts website
cccontracts = urllib2.Request('http://www.clark.wa.gov/contracts-grid/')

## make a handler to use with spoofer
opener = urllib2.build_opener()
## spoof browser user agent so the website doesn't think we are a bot
cccontracts.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0')

## have handler open website with spoofed user agent and read website
contracts = opener.open(cccontracts).read()
## run output into beautifulsoup 
soup = BeautifulSoup(contracts)
## find locations of contract info and contract pdfs
contract = soup.find_all("td", class_="views-field views-field-field-local-fund-amount")
contract1 = soup.find_all("td", class_="views-field views-field-body-1")
## write to text file
text_file = open('swwawatchdog.html', 'w')

## uses a for loop to grab, save and print pdf file url, uses another for loop on info about contract

final = {}
i = 0
i2 = 2

text_file.write('<html><head><meta charset="UTF-8"><link rel="stylesheet" type="text/css" href="/css/swgs.css"><title>SouthWest WAshington Watchdog</title></head><body><script src="https://code.jquery.com/jquery-3.1.0.js"integrity="sha256-slogkvB1K3VOkzAI8QITxV3VzpOnkeNVsKvtkYLMjfk="crossorigin="anonymous"></script>' + 
                """
<script type="text/javascript">
    $(document).ready(function(){
        $('.title1').addClass("visible");


        $('.title1').click(function() {
            var $this = $(this);

            if ($this.hasClass("hidden")) {
                $(this).removeClass("hidden").addClass("visible");

            } else {
                $(this).removeClass("visible").addClass("hidden");
            }
            });
        });
    $(document).ready(function(){
        $('.title2').addClass("visible");


        $('.title2').click(function() {
            var $this = $(this);

            if ($this.hasClass("hidden")) {
                $(this).removeClass("hidden").addClass("visible");

            } else {
                $(this).removeClass("visible").addClass("hidden");
            }
            });
        });

</script>""" + '</class><div class="title1" id="title1">CLARK COUNTY<div class="clark" id="clark">'.encode('utf-8'))


for x in contract1:
    thing = '<div id="clarkc' + str(i) + '"> <a href="https://www.clark.wa.gov' + x.a['href'] + '">' + x.get_text('') + '</a><br>' + contract[i].get_text(' ') + "</div>"
    final[i] = thing
    i += 1


for each in final:

    text_file.write(final[each].encode('utf-8')) 


time.sleep(5)

clarkMeetings = "https://www.clark.wa.gov/the-grid"
clarkM = urllib2.Request(clarkMeetings)
clarkM.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0')
clarkMeet = opener.open(clarkM).read()
clarkSoup = BeautifulSoup(clarkMeet)
clarkLinks1 = clarkSoup.find_all('td')
clarkLinks2 = {}
clarkLinks3 = {}
clarkLinks4 = {}
i3 = 0
i4 = 0
i5 = 0
i6 = 0
for each in clarkLinks1:
#    if each == None:
#        clarkLinks2[i3] = " "
#    else:
        clarkLinks2[i3] = '<br>' + each.get_text(" ", strip=True) + '<br>'
        i3 += 1
   

for each in clarkLinks1:
#    if each == None:
#        print " "
#    else:
        clarkLinks3[i4] = each.a
        i4 += 1

clarkLinksEtc = {} 
for each in clarkLinks3:
    if clarkLinks3[each] == None:
        clarkLinks4[i5] = " "
    else:
        x = clarkLinks3[each]
        x1 = str(x).split('/sites')

        if '/sites' in str(x):
            
            
            x1.insert(1, 'https://www.clark.wa.gov/sites')
            x2 = "".join(x1)
            x3 = x2.split('"')
            clarkLinksEtc[i5] = x3[1]
            clarkLinks4[i5] = x2
            i5 += 1
        else:
            clarkLinks4[i5] = x
            

print clarkLinksEtc #pdfs to crawl for info

for each in clarkLinks4:
    if clarkLinks4[each] == ' ':
        i6 += 1

    else:         
        
        text_file.write('<div id="clark2' + str(i6) + '">'.encode('utf-8'))
        text_file.write(clarkLinks4[each].encode('utf-8'))
        text_file.write(clarkLinks2[each].encode('utf-8'))
        text_file.write('</div>'.encode('utf-8'))
        i6 += 1
        
text_file.write('</div></div><div class="title2" id="title2">VANCOUVER<div id="vanc">'.encode('utf-8'))

vanMonth = "http://www.cityofvancouver.us/meetings?date_filter[value][month]=" + str(nowmonth) + "&date_filter[value][day]=1&date_filter[value][year]=" + str(nowyear) + "&date_filter_1[value][month]=" + str(nowmonth) + "&date_filter_1[value][day]=30&date_filter_1[value][year]=2016&field_synonym_value=All&term_node_tid_depth=All"
vancouver = urllib2.Request(vanMonth)
vancouver.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0')
vancouverc = opener.open(vancouver).read()
vanSoup = BeautifulSoup(vancouverc)

url1 = vanSoup.find_all("td", class_="views-field views-field-view-node")

links = {}
j1 = 0

van = {}



   
for each in url1:
	links[j1] = "http://www.cityofvancouver.us" + each.a['href']
	j1 += 1
j2 = 1
for each in links:

    van[each] = urllib2.Request(links[each])
    van[each].add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0')
    van1 = opener.open(van[each]).read()
    van1Soup = BeautifulSoup(van1)
    for g in van1Soup.find_all('h1', id='page-title'):
        g.extract()
    for b in van1Soup.find_all('a', href='/meetings'):
        b.extract()
    for t in van1Soup.find_all('div', class_='location clear-left'):
        t.extract()
    van1Title = van1Soup.find('title')
    van1TitleText = van1Title.get_text()
    van1Words = van1Soup.find_all('div', class_="no_sidebar")
    for each1 in van1Words:
        text_file.write('<div id="vancouver' + str(j2) + '">'.encode('utf-8'))
        text_file.write('<h5><a href="' + str(links[each]) + '">' + str(van1TitleText) + '</a></h5>'.encode('utf-8'))
        j2 += 1
        
        printThis = each1.get_text('<br>')
        text_file.write(printThis.encode('utf-8'))
        text_file.write('</div>'.encode('utf-8'))
        
    time.sleep(5)
    print str(each) + " done"


            


text_file.write("</div></div>".encode('utf-8'))
text_file.write("</body></html>".encode('utf-8'))
text_file.close()
ftpSession = ftplib.FTP('host', 'username', 'password')
uploadFile = open('swwawatchdog.html','rb')
ftpSession.cwd('62dodgedart.com')
ftpSession.storbinary('STOR swwawatchdog.html', uploadFile)
uploadFile.close()                                    
ftpSession.quit()

