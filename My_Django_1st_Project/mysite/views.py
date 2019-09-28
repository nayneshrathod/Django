from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def home(request):
    return HttpResponse('''
    <h1>This is my Index Page</h1><br>
    <a href="/home">home</a><br/>
    <a href="/analyze">analyze</a><br/>
    <a href="/about">about</a><br/>
    <a href="/charcount">char count</a><br/>
    <a href="/spaceremove">space remover</a><br/>
    <a href="/removepunk">remove punkcuation</a><br/>
    <a href="/newremoveline">new remove line</a><br/>
    <a href="/capitalizefirst">capitalize first</a><br/>
    ''')


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("<h1>This is my About Page</h1><button> <a href='/'>back </a></button>")


def analyze(request):
    # get The Text
    djtext = request.POST.get('text', 'default')
    charcount = request.POST.get('charcount', 'Off')
    removepunc = request.POST.get('removepunc', 'Off')
    spaceremove = request.POST.get('spaceremove', 'Off')
    newremoveline = request.POST.get('newremoveline', 'Off')
    capitalizefirst = request.POST.get('capitalizefirst', 'Off')

    # analyed = djtext
    if removepunc == "on":
        analyed = ""
        punc = '''!(){}[]=-_"';:,.<>?/\|@#$%^&*~`+'''
        for char in djtext:
            if char not in punc:
                analyed = analyed + char
        param = {'purpose': 'Remove Puncuation', 'anaylied_text': analyed }
        djtext = analyed
        # return render(request, 'anaylze.html', param)
    if spaceremove == "on":
        analyed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyed = analyed + char
        param = {'purpose': 'Remove Space', 'anaylied_text': analyed }
        djtext = analyed
        #        return render(request,'anaylze.html', param)
    if newremoveline == "on":
        analyed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyed = analyed + char
        param = {'purpose': 'Remove New Line', 'anaylied_text': analyed }

        djtext = analyed
        #        return render(request,'anaylze.html', param)
    if capitalizefirst == "on":
        analyed = ""
        for char in djtext:
            analyed = analyed + char.upper()
        param = {'purpose': 'Change to Uppercase ', 'anaylied_text': analyed}

        djtext = analyed
        #        return render(request,'anaylze.html', param)
    if charcount == "on":

        c = "Count : "
        count = len(djtext)
        param = {'purpose': 'Length Of Charctor ', 'anaylied_text': djtext,'cc' :c, 'count': count}

        # djtext = param
        #        return render(request, 'anaylze.html', param)
    if (capitalizefirst != "on" and charcount != "on" and newremoveline != "on" and spaceremove != "on" and removepunc != "on"):
        return HttpResponse("<H1>Error</h1>")

    return render(request, 'index.html', param)


def removepunk(request):
    # #get The Text
    # djtext = request.GET.get('text','default')
    # print(djtext)
    return HttpResponse("<h1>This is my remove punkcuation Page</h1><button> <a href='/'>back </a></button>")


def capitalizefirst(request):
    return HttpResponse("<h1>This is my capitalize first Page</h1><button> <a href='/'>back </a></button>")


def newremoveline(request):
    return HttpResponse("<h1>This is my  new remove line Page</h1><button> <a href='/'>back </a></button>")


def spaceremove(request):
    return HttpResponse("<h1>This is my space remove Page</h1><button> <a href='/'>back </a></button>")


def charcount(request):
    return HttpResponse("<h1>This is my char count Page</h1><button> <a href='/'>back </a></button>")

def contactus(request):
    return render(request,'contactus.html')
