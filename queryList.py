# creates a list of search terms
def queryList(d):
    terms = []
    if 'names' in d.keys():
        terms += d['names']
    for n in d['names']:
        if 'addresses' in d.keys():
            for l in d['addresses']:
                terms.append(n+' '+l)
            for a in d['activities']:
                terms.append(n+' '+a)
    return terms
