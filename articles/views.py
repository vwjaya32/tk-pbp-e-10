from nntplib import ArticleInfo
from django.shortcuts import render
from django.shortcuts import redirect
from articles.models import *
from django import forms

# Create your views here.
class edit_box(forms.Form):
    author = forms.CharField(label="Author", widget=forms.TextInput(attrs={'size': 37}))
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={'size': 37}))
    content = forms.CharField(label="Content", widget=forms.Textarea)

def show_articles(request):
    articles_list = Articles.objects.all()
    context = {
        'data': articles_list,
    }
    return render(request, "articles.html", context)

def write_articles(request):
    if request.method == "POST":
        forms = edit_box(request.POST)
        if forms.is_valid():
            new_artc = Articles(
                title = forms.cleaned_data["title"],
                author = forms.cleaned_data["author"],
                content = forms.cleaned_data["content"],
            )
            new_artc.save()
            return redirect("articles:show_articles")

    forms = edit_box()
    context={"form":forms}
    return render(request, "write.html", context)