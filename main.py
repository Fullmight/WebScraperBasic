# import Libraries
import unicodecsv as csv
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

# specify the url
quote_page = 'http://www.wowstats.org/ships/'

# query website and return html to variable 'page'
page = urlopen(quote_page)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# remove the <div> of name and return its value
name_box = soup.find('title')

#if name_box:
    #name = name_box..strip()  # strip() removes starting and trailing
    #print(name)

# get index price

price_box = soup.find('tr', {"style":"height:35px;"})
if price_box:
    price = price_box.get_text(separator=':').encode("utf-8")
    #print(price)

finalList = price.splitlines()

for z in range(len(finalList)):
    interIter = finalList[z]
    finalList[z] = interIter.decode("utf-8")#.replace(',','',1)
    print(finalList[z])
    #for i, c in enumerate(finalList[z]):
    #   if c.isdigit():
    #      finalList[z] = finalList[z][:i] + ' ' + finalList[z][i:]
    #     break
    #



#for y in finalList:
    #print(y)

#append Data to a CSV file
with open('index.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file, encoding='utf-8')
    for x in finalList:
        writer.writerow([x, datetime.now()])

