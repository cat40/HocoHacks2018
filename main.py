import search, Input, analyze, queryList
import cPickle as pickle
import frequencies

attributes = Input.takeInput()

try:
    with open('found.pkl', 'r') as f:
        found = pickle.load(f)
except IOError: found = []

name = attributes['names'][0].split(' ')[1] #get last name

for query in queryList.queryList(attributes):
    #print query
    results = list(analyze.analyze(search.getSearch(query), attributes, frequencies.getLevels(name)))
    for url, result in results:
        if url not in found:
            found.append(url)
            print 'New item found! The website %s contains references to you' % url
print 'done searching'

with open('found.pkl', 'w') as f:
    pickle.dump(found, f)
            
    
