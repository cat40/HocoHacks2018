'''
Created on Apr 14, 2018

@author: Zeros
'''
import cPickle as pickle

def takeInput():
    try: attributes = pickle.load('config')
    except IOError: pass
    else: return attributes
        return
    attributes = dict()
    print "This is a program that checks if google has updated information on yourself"
    print "Input a list of activities, addresses etc. \n(use 'end' to stop inputting parameters)")
    for par in ('names', 'activities', 'addresses'):
        attributes[par] = #input thing
    pickle.dump(attributes, 'config')
    return attributes


if __name__ == '__main__':   
    takeInput()
    file = open("config", "r")
    print(file.readlines())


urls = search()
return zip(urls, (htmlget(url) for url in urls))
