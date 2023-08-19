from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.
def index(request):
    return render(request,"singlepage/index.html")

text = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore",
    "magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea", "commodoconsequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla", "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
]
def sections(request,num):
    if 1<= num <= 4:
        return HttpResponse(text[num-1])
    else:
        raise Http404("No such section")