from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'home.html')

def translate(request):

    orginal = request.GET["orginaltext"].lower()

    translation = ''

    for word in orginal.split():
        if word[0] in['a','e','i','o','u']:

            #vowel
             translation += word
             translation += 'yay'


        else:
            translation += word[1:]
            translation += word[0]
            translation +='ay'






    return render(request, 'translate.html', {'orginal': orginal, 'translation':translation})





def about(request):
    return render(request, 'about.html')






