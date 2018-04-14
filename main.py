import search, Input, analyze
import cPickle as pickle

attributes = Input.takeInput()

try:
    with open('found.pkl', 'r') as f:
        found = pickle.load(f)

for query in attributes['name']#queryList(attributes):
    results = list(analyze.analyze(search.getSearch(query), attributes))
    for url, result in results:
        if url not in found:
            found.append(url)
            print 'New item found! The website %s contains references to you' % url

with open('found.pkl', 'w') as f:
    pickle.dump(found, f)
            
    
