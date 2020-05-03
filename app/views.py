from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import KeywordForm, AcctForm
from .models import AcctModel, KeywordModel

# Create your views here.

class Account(View):
    

    def get(self, request, *args, **kwargs):
        """GET用メソッド"""
        form = AcctForm()
        fb_all = AcctModel.objects.filter(category = 1)
        weibo_all = AcctModel.objects.filter(category = 2)
        message = "hello"
        context = {
            'form': form,
            'fb_all': fb_all,
            'weibo_all': weibo_all,
        }
        return render(request, 'app/account.html', context)

    def post(self, request, *args, **kwargs):
        """POST用メソッド"""
        form = AcctForm()
        fb_all = AcctModel.objects.filter(category = 1)
        weibo_all = AcctModel.objects.filter(category = 2)
        message = "hello"
        context = {
            'form': form,
            'fb_all': fb_all,
            'weibo_all': weibo_all,
        }
        acctform = AcctForm(request.POST)
        if acctform.is_valid():
            post = acctform.save(commit=False)
            post.save()

        return render(request, 'app/account.html', context)


class Keyword(View):
    def get(self, request, *args, **kwargs):
        """GET用メソッド"""
        return render(request, 'app/keyword.html')

    def post(self, request, *args, **kwargs):
        """POST用メソッド"""
        return render(request, 'app/keyword.html')

class Time(View):
    def get(self, request, *args, **kwargs):
        """GET用メソッド"""
        return render(request, 'app/time.html')

    def post(self, request, *args, **kwargs):
        """POST用メソッド"""
        return render(request, 'app/time.html')