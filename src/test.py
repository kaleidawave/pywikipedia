from pywikipedia import wikipedia
from tabulate import tabulate

#page = wikipedia.WikiPage("Python (Programming Language)") #argument is the last part of wikipedia URL - will fixed underscored later

page = wikipedia.search("Train")

#print(page.title) # prints title
#print(page.lastedited.strftime("%Y-%m-%d %H:%M")) #prints time of last edit as datetime object
#print(page.tables) # prints list of tuples -> (contentnum, contenettitle)
#print(page.paragraphs[:3]) #prints first 3 paragraphs
#print(tabulate(page.infobox)) #prints first 3 paragraphs

#print(page.section('Politics'))

print("Done") #testing for finish