from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'index.html')
def submits(request):
    if request.method == 'GET' and 'count' in request.GET:
        # To pass whole html we use template
        usertext = request.GET['usertext']
        #print(usertext)
        wordList = usertext.split()
        wordDic = {}
        for word in wordList:
            if word in wordDic:
                #increasing number
                wordDic[word] += 1
            else:
                #add new wordDic
                wordDic[word] = 1
        return render(request,'count.HTML',{'usertext':usertext,
                              'Words': len(wordList),
                              'wordDic': sorted(wordDic.items(), key = operator.itemgetter(1), reverse = True)})
    if request.method=='GET' and 'about' in request.GET:
        return render(request,'about.html')
