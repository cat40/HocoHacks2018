def analyze(results, user):
    '''
    in this order:
    check if url is on the blacklist
    check if the user's name or usernames are in the result
    check activities
    '''
    for result in results:
        if isrelevent(result, user):
            yield result

#equilivnet to 'return url not in user.blacklist and any(name in text for name in names) and any(acitivity in user.activitys)
#will return false if user doesn't have any relevent keys
def isrelevent(result, user, level):
    url, text = result
    #check url
    if 'blacklist' in user.keys() and url in user['blacklist']:
        return False
    #make sure one of the user's names is in the website
    if level==0:
        if 'names' in user.keys() and not any(name in text for name in user['names']):
            return False
        #check activities
        return'activities' in user.keys() and any(activity in text for activity in user['activities'])
    elif level==1:
        if 'names' in user.keys() and any(name in text for name in user['names']):
            return True
        return'activities' in user.keys() and any(activity in text for activity in user['activities'])
    else:
        if 'names' in user.keys() or any(name in text for name in user['names']):
            return True
        return'activities' in user.keys() and any(activity in text for activity in user['activities'])

