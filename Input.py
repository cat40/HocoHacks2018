'''
Created on Apr 14, 2018

@author: Zeros
'''
import cPickle as pickle


def takeInput():
    try:
        with open('config') as f: 
            attributes = pickle.load(f)
    except IOError: pass
    else: return attributes
    attributes = dict()
    
    print "This is a program that checks if google has updated information on yourself"
<<<<<<< HEAD
    print "Input a list of names, activities, addresses etc. \n(use 'end' to stop inputting parameters)"
    
    nameList = []
    activitiesList = []
    addressesList = []
    i = 1
    while True :
        inp = raw_input("name " + str(i) + ": ")
        if(inp == "end"):
            break
        else:
            nameList.append(input)
        i += 1
    i = 1
    while True :
        inp = raw_input("addresses " + str(i) + ": ")
        if(inp == "end"):
            break
        else:
            addressesList.append(input)
        i += 1
    i = 1
    while True :
        inp = raw_input("activities " + str(i) + ": ")
        if(inp == "end"):
            break
        else:
            activitiesList.append(input)
        i += 1
    attributes["name"] = nameList
    attributes["activities"] = activitiesList   
    attributes["addresses"] = addressesList 
    
    with open('config', 'w') as f:
        pickle.dump(attributes, f)
=======
    print "Input a list of activities, addresses etc. \n(use 'end' to stop inputting parameters)")
    for par in ('names', 'activities', 'addresses'):
        attributes[par] = #input thing
    pickle.dump(attributes, 'config')
>>>>>>> 01cb6c931e5b63aa863053c607daf5ab0646705f
    return attributes


if __name__ == '__main__':   
    takeInput()
    file = open("config", "r")
    print(file.readlines())
