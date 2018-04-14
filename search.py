import googlesearch
import urllib


def getHTML(url):
    try:
        html = urllib.urlopen(url)
        return html.read()
    except IOError, e:
        # if e.errno == 10054:
        print e
        return ''

    
def getSearch(query):
    for u in googlesearch.search(query, num=5, stop=1):  # , pause=10):
        print u
        h = getHTML(u)
        yield u, h
