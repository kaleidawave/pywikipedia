# Wikipedia Python Package

I was annoyed how many python wikipedia packages there are. They all have a lot of users but all are undermaintained, underdocumented and broken. I want to change this by implementing a package which has all the functionality of various packages while also being up to date and active.

Currently in development stages. Coming to PyPi soon....

## Current features:

- Retrieve a page based on the affix of the wikipedia url

    > page = wikipedia.WikiPage("Python_(Programming_Language)")

- Return title of page

    > page.title -> 'Python (programming language)'

- Return content by paragraphs

    > page.paragraphs[:3] -> ['Python is ...',' ... ', ...

- Return contents of page in zipped form

    > page.contents -> [('1', 'History'), ('2', 'Features and philosophy'), ('3',...
