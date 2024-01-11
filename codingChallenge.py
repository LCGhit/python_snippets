import math
import re

def readNumber(file):
    theText = open(file, "r")
    values = re.findall("[a-zA-Z]+", theText.read())
    theText.close()
    theText = open(file, "r")
    keys = re.findall("[0-9]+", theText.read())
    theText.close()
    theDict = dict()
    for i in range(len(keys)):
        theDict[keys[i]] = values[i]
    theDict = dict(sorted(theDict.items()))
    outputMsg = ""
    for i in range(0, math.floor(len(keys)/2)):
        outputMsg = outputMsg+" "+theDict[str(i+i+1)]
    print(outputMsg)
