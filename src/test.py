from pywikipedia import wikipedia
from tabulate import tabulate

page = wikipedia.WikiPage("Barack_Obama") #argument is the last part of wikipedia URL - will fixed underscored later

#print(page.title) # prints title
#print(page.contents) # prints list of tuples -> (contentnum, contenettitle)
#print(page.paragraphs[:3]) #prints first 3 paragraphs
print(tabulate(page.infobox)) #prints first 3 paragraphs

print("Done") #testing for finish
