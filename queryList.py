# creates a list of search terms
def queryList(d):
    terms = []
    for nameOnly in d['names']:
        terms.append(nameOnly)
    for n in d['names']:
        for l in d['addresses']:
            for a in d['activities']:
                terms.append(n+' '+l+' '+a)
    return terms
