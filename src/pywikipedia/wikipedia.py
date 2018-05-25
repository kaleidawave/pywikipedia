import requests
from bs4 import BeautifulSoup


#need buffer for disambigous errors
class WikiPage():
    def __init__(self, url):
        result = requests.get("https://en.wikipedia.org/wiki/" + url)
        if result.status_code == 200: print("Found")

        soup = BeautifulSoup(result.content, "lxml")

        self.run(soup)
    
    def run(self, html):
        #sets all class variables up 

        #retrives title (Done)
        self.title = html.select("#firstHeading")[0].text

        #main content section
        content = html.select('#mw-content-text > div')[0]

        #returns contents list
        rawcontents = list()
        for element in content.select('#toc > ul')[0].findChildren('span'):
            rawcontents.append(element.text)
        self.contents = list(zip(rawcontents[::2], rawcontents[1::2],)) 

        #paragraphs (Done)
        self.paragraphs = list()
        for element in content.select('p'):
            self.paragraphs.append(element.text) #may added regex to fix refence numbers being added

        #summary box (Not Done)
        try: infobox = html.select('#mw-content-text > div > table.infobox') #some vevent others vcard
        if infobox[0] is None:
            self.info = False
        else:
            self.info = True
            self.infobox = list()
            for row in infobox[0].find_all('tr'):
                rowlist = list()
                try: rowlist.append(row.find('th').text)
                except: rowlist.append("")
                for column in row.find_all('td'):
                    rowlist.append(column.text)
                    
                self.infobox.append(rowlist)     

        #future variables
        self.tables = None
        self.images = None
        self.sections = None
        self.url = None
        self.datecreated = None
        self.haspanel = None

    #future methods 
    def table(self, table):
        pass
        #return tables[table]
    
    def section(self, section):
        pass
        #return sections[section].text()

    def image(self, image):
        pass
        #return images[images].url()

    def text(self, paragraphs = 2):
        pass
        #return text