from django.shortcuts import render
from     django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def analyze(request):
    # text 
    djtext = request.POST.get('text','default')
    punc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newline = request.POST.get('newline','off')
    space = request.POST.get('space','off')
    counter = request.POST.get('counter','off')



    # check which checkbox in on
    if punc =='on':
        puntuation = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyze = ""
        for char in djtext:
            if char not in puntuation:
                analyze = analyze + char
                context ={
        'purpose':'Remove Punctuations',
        'analyze_text':analyze
    }
        djtext = analyze
    if(fullcaps=='on'):
        analyze = ''
        for char in djtext:
            analyze = analyze + char.upper()
            context ={
        'purpose':'Upper Case',
        'analyze_text':analyze
    }
            djtext = analyze
    if(newline=='on'):
        analyze = ''
        for char in djtext:
            if char !='\n' and char !='\r':
                analyze = analyze + char
                context ={
        'purpose':'Remove New Lines',
        'analyze_text':analyze
    }
                djtext = analyze
    if(space=='on'):
        analyze = ''
        for index, char in enumerate(djtext):
            if not (djtext[index] ==" " and djtext[index+1]==" "):
                analyze = analyze + char
                context ={
        'purpose':'Space Remover',
        'analyze_text':analyze
    }
                djtext = analyze
    if(counter=='on'):
        analyze = 0
        for index, char in enumerate(djtext):
            analyze = analyze + 1
            context ={
        'purpose':'Total Char Counter',
        'analyze_text':f"{analyze}"
    }
   
    return render(request,'analyze.html',context)