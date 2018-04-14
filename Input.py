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
            nameList.append(inp)
        i += 1
    i = 1
    while True :
        inp = raw_input("addresses " + str(i) + ": ")
        if(inp == "end"):
            break
        else:
            addressesList.append(inp)
        i += 1
    i = 1
    while True :
        inp = raw_input("activities " + str(i) + ": ")
        if(inp == "end"):
            break
        else:
            activitiesList.append(inp)
        i += 1
    i = 1
    attributes["name"] = nameList
    attributes["activities"] = activitiesList   
    attributes["addresses"] = addressesList 
    
    blackList = []
    
    print("Please input site names that you know you have an account of \nsuch as Facebook, Instagram etc. (use end to stop)")
    while True :
        inp = raw_input("Blacklist " + str(i) + ": ")
        if(inp == "end"):
            break
        else:
            blackList.append(inp)
        i += 1
    attributes["Blacklist"] = blackList
    
    with open('config', 'w') as f:
        pickle.dump(attributes, f)
    return attributes


if __name__ == '__main__':   
    takeInput()
    # #with open('config') as f: 
    # #     print(pickle.load(f))
