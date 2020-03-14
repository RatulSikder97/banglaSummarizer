import nltk,score,math,preprosess
'''
    
    ##semantic analysis
        i) strip suffix from each sentence(lightweight stemming)
        ii)find similarity
        iii)if similar remove low scored 
    '''
#suffix striping:::::
def suffixSt(word):
    # suffix dictionary
    suffix = {
        1: [u"ি", u"ই", u"আ", u"ো", u"া", u"ঈ", u"ই", u"অ", u"ও", u"এ",
            u"র", u"য়", u"ব", u"স", u" ঊ", u"ু", u"ো", u"ে", u"ী", u"য়", u"ক", "য়", "ল", "ছ", "ব"],
        2: [u"য়ে", u"না", u"লি", u"নি", u"না", u"য়া", u"ায়", u"ড়ি", u"িস", u"ান", u"ের", u"ার", u"ান", u"কু", u"কা",
            u"বি",
            u"তে", u"রা", u"বে", u"মি",
            u"সি", u" আল", u" উক", u"ড়ে", u"কে", u"টা", u"টি", u"টু", u"কা", u" রি", u"তি", " তা", "িল", "িক", "েক",
            "েত", "েই", "আও", "আন", " আত", " আই", " অন", " অত", " অক", "ড়ে", "ড়ি", "ড়া", "সে", "সা", "লা", "মি",
            "ভর", "নি", "তি", "তা", "টে", "টা", "চে", "কে", "কা", "এল", "উড়", "উক", "আল", "আর", "আম", "আত", "আচ", "আই",
            "অড়", "অল", "তো",
            "েছ", "েল", "ছে","েও"],
        3: ["ওয়া", " উরি", "উয়া", "উনি", "উকা", u"দের", "য়ের", "কায়", "কার", "েরা",
            "িলা", "িনি", "তেই", "টাই", "ইয়ে", " ইয়া", " ইলে", " আরী", " আরি", u"আনো", " আনি", " আকু", " আইত",
            " অন্ত", " অনি", " অনা", " অতি", " অতা", " োয়া", "ুয়া", "ুন্তি", "ুনি", "ুকা", "ুকা", "সিয়", "মন্ত", "ভরা",
            "য়োন", "খান", "গুল", "পনা", "তুত", "উয়া", "উলি", "উরে", "ইয়া", "আলো", "আলি", "আলা", "আরু", "আরি", "আমো",
            "আমি",
            "আনো", "আনি", "আচি", "আইত",
            "চ্ছ", "েছে", "েলো", "ওয়া", "মান"],
        4: [u"েদের", " অন্তি", "টিয়া", "কিয়া", " উন্তি", u"য়েরা", u"ভাবে", "খানা", "খানি", "গুলো", "গুলি", "পারা",
            "পানো",
            "ইয়াল", "য়েছে", "চ্ছি", "চ্ছে", "েছেন"],
        5: [u"দেরকে", "চ্ছিল", "চ্ছিস", u"য়েদের", "ওয়ালা", "উড়িয়া"],
        6: [u"েদেরকে", "চ্ছিলেন"],
        7: [u"য়েদেরকে"]
    }
    for w in 7, 6, 5, 4, 3, 2, 1:
        if len(word) > w + 1:
            for s in suffix[w]:
                if word.endswith(s):
                    return word[:-w]
    return word


#make one sent list:::::
def makeList(sent):
    tok=nltk.word_tokenize(sent)
    li=[]
    for w in tok:
        li.append(suffixSt(w))
    return li

#making total list:::::::
def makeTolist(allsent):
    lst=[]
    for sen in allsent:
        lst.append(makeList(sen))
    return lst

##Get cosine
def get_cosine(vec1, vec2):
    #here A n B
    intersection = set(vec1.keys()) & set(vec2.keys())
    #dot product of teo sentence
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])

    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    #avoid null space vectors
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

#cosine similarity check for all passage
"""
check all sentence 2d  matrix  form

"""
def getCoVal(allItm,priSum):
    n=len(allItm)
   # print(allItm)
    cos=[]
    algn1=[]
    algn2=[]
    cos.append(" "+priSum[0])
    for i in range(0,n):
        for j in range(i+1,n):
            vec1=score.scoreWord(allItm[i])
            vec2=score.scoreWord(allItm[j])
            cosi=get_cosine(vec1,vec2)
            #sentences set gen exceptin 95% simalarity sentence
            if cosi<0.95 and priSum[j] not in cos:
                cos.append(priSum[j])
    return cos


'''
  
'''
def finalSummary(priSummary):
    stemmedList = makeTolist(priSummary)
    final = getCoVal(stemmedList, priSummary)
    finalText = " । \n".join(final) + "।"

    return finalText
