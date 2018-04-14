import googlesearch
import urllib
def getHTML(url):
    html = urllib.urlopen(url)
    return html.read()
def getSearch(query):
    for u in googlesearch.search(query, num=25, stop=1):
        print u
        h = getHTML(u)
        yield u, h
