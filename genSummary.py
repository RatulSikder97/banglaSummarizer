"""
primary summary hold main documents sentence position

"""
import math,sys

def genSummary(sent,scDict):
    maxVal = max(scDict.values())
    s=sum(scDict.values())
    #70% of passage
    per=(s/len(scDict))
    print("Max score: "+str(maxVal))
    print(per)
    print("Length of texts: "+ str(len(scDict)))
    summary = []
    for s in sent:
        if scDict[s] >= per:
            summary.append(s)

    return summary





