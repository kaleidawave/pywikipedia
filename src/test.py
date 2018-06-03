from pywikipedia import wikipedia
from tabulate import tabulate

wikipedia.date_as_string = True

page = wikipedia.random()

print(page.title)
print(page.lastedited) 
#print(page.paragraphs[:3])
#print(page.contents[0])

#print(page.section(page.contents[0]))
