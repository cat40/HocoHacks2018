def analyze(results, user):
    '''
    in this order:
    check if url is on the blacklist
    check if the user's name or usernames are in the result
    check activities
    '''
    for result in results:
        yield result, isrelevent(result, user)


#equilivnet to 'return url not in user.blacklist and any(name in text for name in names) and any(acitivity in user.activitys)
def isrelevent(result, user):
    url, text = result
    #check url
    if url in user.blacklist:
        return False
    #make sure one of the user's names is in the website
    if not any(name in text for name in names):
        return False
    #check activities
    return any(activity in text for activity in activities)
    
