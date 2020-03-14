import nltk
import re,math

#tokenizer
def wordToke(text):
    word=[]
    for x in text:
        token=x.split()
        word+=token
    return word

#Unknown remove
def prePunc(file):
    sentence = file.split(u'।')
    #print(sentence)
    sentence = [i.replace(u'\ufeff', '') for i in sentence]

    return sentence


#puntuation remove
def puncRem(words):
    pnList = ['.', ',', ':', '(', ')', '[', ']', '{', '}', '`', '*', '&', '‘', '’', '–']
    filtPunc = [w for w in words if w not in pnList]

    return  filtPunc


#remove stopword
def remStWors(punctuF):
    stWord = open("./stopwords-bn.txt", encoding='utf8')
    stWordFile = [i.rstrip() for i in stWord]
    filtStWord = [w for w in punctuF if w not in stWordFile]

    return filtStWord

