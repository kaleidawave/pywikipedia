Download now using pip!! `pip install pywikipedia`

# Wikipedia Python Package

I was annoyed how many python wikipedia packages there are. They all have a lot of users but all are undermaintained, underdocumented and broken. I want to change this by implementing a package which has all the functionality of various packages while also being up to date and active.

Currently in development stages

Source can be found in the src folder

## Using pywikipedia:

First download using pip 

    pip install pywikipeida

And import the package:

    from pywikipedia import wikipedia

- Retrieve a page from wikipedia:

	Through google search:

       page = wikipedia.search("Python code")
	   
	Or picking a random page:
	
	   page = wikipedia.random()
	   
	Or picking the page featured on the main page:
	
	   page = wikipedia.featured()
	   
	Or finally, picking the page associated with today:
	
	   page = wikipedia.today()

- Return title of page

       page.title -> 'Python (programming language)'

- Return content by paragraphs

       page.paragraphs[:3] -> ['Python is ...',' ... ', ...

- Return contents of page in zipped form

       page.contents -> [('1', 'History'), ('2', 'Features and philosophy'), ('3',...

- Sections can then be found from the page

       page.section(1) -> ["History", "Python was con...]..

    or

       page.section("History") -> ["History", "Python was con...]..

    or finally

       page.section(('1', 'History')) -> ["History", "Python was con...]..

    there is also an optional argument that when set to false doesn't include the section heading

- Find the date of the last edit

       page.lastedited -> <Datetime object.....>

    optionally setting `wikipedia.date_as_string = True` will return a string rather than datetime:

       This page was last edited on 1 January 2018, at 22:13.

## About

This package works in `python 3.6.2`  and requries `beautfulsoup 4.6`, `lxml` and `requests 2.11` (all should be installed during pip installation)

Any issues recieved please post to the issues tab on github, thanks :)
