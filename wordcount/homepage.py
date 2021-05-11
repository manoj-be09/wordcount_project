from django.http import HttpResponse
from django.shortcuts import render
import operator

def word_count(request):
    return render(request,'homepage.html')


def count(request):
    fulltext=request.GET['input_text']
    fulltext_list=fulltext.split()
    text_dict= {}
    for text in fulltext_list:
        if text in text_dict:
            text_dict[text]+=1
        else:
            text_dict[text]=1
        
    sorted_words=sorted(text_dict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'input_dict': sorted_words , 'count':len(fulltext_list),'fulltext':fulltext})


def about(request):
    return render(request,'about.html')


