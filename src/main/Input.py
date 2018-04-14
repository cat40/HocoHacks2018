'''
Created on Apr 14, 2018

@author: Zeros
'''


def takeInput():
    file = open("config", "r")
    filelines = file.readlines()
    if(len(filelines) > 1):
        print(filelines)
        file.close()
    file = open("config", "a")
    print("This is a program that checks if google has updated information on yourself")
    print("Input a list of activities, addresses etc. \n(use 'end' to stop inputting parameters)")
    condition = False
    i = 1
    
    while condition == False :
        inp = input("input " + str(i) + ":")
        if(inp == "end"):
            condition = True
        else:
            file.write(inp + "\n")
        i += 1
    print("Your data has been stored")
    file.close   


if __name__ == '__main__':   
    takeInput()
    file = open("config", "r")
    print(file.readlines())