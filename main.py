# import Libraries
import unicodecsv as csv
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

# specify the url
page_url = 'http://www.wowstats.org/ships/'

# query website and return html to variable 'page'
page = urlopen(page_url)

# parse the html using beautiful soup and store in variable 'soup'
soupObj = BeautifulSoup(page, 'html.parser')

# remove the <div> of name and return its value
siteName = soupObj.find('title')

#site name test print
#if name_box:
    #name = name_box..strip()  # strip() removes starting and trailing
    #print(name)

# get index price

# Whatever your key information is, it goes in here. create more
# in the same Vein if needed.
coreDataVar = soupObj.find('tr', {"style": "height:35px;"})
if coreDataVar:
    price = coreDataVar.get_text(separator=':').encode("utf-8")
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

