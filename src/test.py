from pywikipedia import wikipedia


page = wikipedia.WikiPage("Python_(Programming_Language)") #argument is the last part of wikipedia URL - will fixed underscored later

print(page.title) # prints title
print(page.contents) # prints list of tuples -> (contentnum, contenettitle)
print(page.paragraphs[:3]) #prints first 3 paragraphs

print("Done") #testing for finish
