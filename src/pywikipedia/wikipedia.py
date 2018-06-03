import requests
from bs4 import BeautifulSoup
from datetime import datetime

date_as_string = False

def search(query):
    #uses google to find page
    google_url = "https://www.google.com/search?q=https://en.wikipedia.org/wiki/%20" + query + "&num=5"
    result = requests.get(google_url)
    soup = BeautifulSoup(result.content, "lxml")
    return WikiPage(soup.find_all('cite')[0].text)

def today():
    todaydate = datetime.now().strftime('%B_%d')
    return WikiPage(todaydate)
    
def random(): #not sure if works 100% of the time
    return WikiPage("https://en.wikipedia.org/wiki/Special:Random")

def featured(): #returns featured article (according to whats on the frontpage)
    result = requests.get("https://en.wikipedia.org/wiki/Main_Page")
    soup = BeautifulSoup(result.content, "lxml")
    tableleft = soup.select('td#mp-left')[0]
    link = tableleft.find('a', attrs={'class': None})
    return WikiPage("https://en.wikipedia.org/" + link['href'])


#need buffer for disambigous errors
class WikiPage():
    def __init__(self, url):
        result = requests.get(url)
        if result.status_code == 200: print("Found")
        else: print("no page found")

        soup = BeautifulSoup(result.content, "lxml")

        #html = soup.prettify("utf-8")
        #with open("output.html", "wb") as file:
        #    file.write(html)

        self.run(soup)
    
    def run(self, html):
        #sets all class variables up
        
        #html 
        self.html = html

        #retrives title (Done)
        self.title = html.select("#firstHeading")[0].text

        #main content section
        content = html.select('#mw-content-text > div')[0]

        #returns contents list
        rawcontents = list()
        try: 
            for element in content.select('#toc > ul')[0].findChildren('span'):
                rawcontents.append(element.text)
            self.contents = list(zip(rawcontents[::2], rawcontents[1::2],))
            self.hascontents = True
        except:
            self.hascontents = False #some pages don't have contents e.g. https://en.wikipedia.org/wiki/Hellinsia_scripta

        #paragraphs (Done)
        self.paragraphs = list()
        for element in content.select('p'):
            self.paragraphs.append(element.text) #may added regex to fix refence numbers being added

        #summary box (Not Done)
        infobox = html.select('#mw-content-text > div > table.infobox') #some vevent others vcard
        if len(infobox) == 0:
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

        #finds tables
        self.tables = list()
        tables_titles = html.select('th.navbox-title')
        for table in tables_titles:
            self.tables.append(table.get_text(separator=' ').strip())   
        
        #images 
        self.images = list()
        images = html.select('img')
        for image in images:
            self.images.append(image['src'])

        self.sections = None
        
        self.lastedited = wikitodatetime(html.select('#footer-info-lastmod')[0].text)
        self.haspanel = None

    #future methods 
    def table(self, table):
        pass
        #return tables[table]
    
    def section(self, section):
        if self.hascontents:
            lists = list(zip(*self.contents))
            if isinstance(section, (float, int)): selectionindex = list(lists[0]).index(section)
            else: selectionindex = list(lists[1]).index(section)

            title = self.html.find(id=(lists[1][selectionindex]))
            nexttitle = title.find_next('h1')

            section_paragraphs = list()

            for tag in title.find_all_next():
                if tag.name is 'p':
                    section_paragraphs.append(tag.text)
                elif tag.name in ('h1', 'h2', 'h3'):
                    break

            return section_paragraphs

    def image(self, image):
        pass
        #return images[images].url()

# Helper Functions 

months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
def wikitodatetime(text):
    components = replace(text[29:], '.,:', ' ').split(' ')
    month = months.index(components[2]) + 1
    return datetime(int(components[3]), month, int(components[1]), int(components[6]), int(components[7]))

#BETTER IMPLEMENTATION OF REPLACE BY KALEIDAGRAPH
def replace(string ,old, new):
    for oldchar in old:
        string = string.replace(oldchar, new)
    return string