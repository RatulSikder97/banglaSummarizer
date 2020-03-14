'''Word scroing
wordscroe = no of time appearance '''
def scoreWord(text):
    wordScDict={}
    for word in text:
        count=1
        if word in wordScDict:
            count+=wordScDict.get(word)
        temp={word:count}
        wordScDict.update(temp)
    return wordScDict

'''Sentense scoring'''
def sentScore(eachSent,wordScore):
    score=0.0
    words=eachSent.split(" ")
    for word in words:
        if word not in wordScore:
            continue
        score+=wordScore.get(word)
    return score

def sentScDict(allSent,wordSc):
    dict={}
    sc=0.0
    for sent in allSent:
       sc=sentScore(sent,wordSc)
       t={sent:sc}
       dict.update(t)
    return dict

def scList(allSent,ws):
    score=[]
    for s in allSent:
        score.append(sentScore(s,ws))
    return score

def sort_dictionary(dictionary):
    # Sort the words from a dictionary in ascending order.
    sorted_ascending = sorted(dictionary, key=dictionary.__getitem__)
    sorted_descending = []
    for item in sorted_ascending:
        sorted_descending.insert(0, item)
    return sorted_descending

