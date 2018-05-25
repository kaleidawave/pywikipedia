from pywikipedia import wikipedia
from tabulate import tabulate

page = wikipedia.WikiPage("New York (City)") #argument is the last part of wikipedia URL - will fixed underscored later

#print(page.title) # prints title
#print(page.contents) # prints list of tuples -> (contentnum, contenettitle)
#print(page.paragraphs[:3]) #prints first 3 paragraphs
#print(tabulate(page.infobox)) #prints first 3 paragraphs

print(page.section('Politics'))

print("Done") #testing for finish
