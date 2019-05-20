from django.shortcuts import render, redirect
from .forms import SearchTitleForm
from .crawling_bs4 import SearchMethod

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = SearchTitleForm(request.POST)
        post = form.save()
        keyword = post.words
        title_list = SearchMethod(keyword)
        return render(request, 'result.html', { 'title_list' : title_list })

    else:
        form = SearchTitleForm()
        return render(request, 'home.html', { 'form':form })


    
    