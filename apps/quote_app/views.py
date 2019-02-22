from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

#THESE ARE THE QUOTE APP VIEWS

def quote(request):
    context = {
        "this_user":User.objects.all(),
        "user" : User.objects.get(id=request.session['user_id']),
        "all_quotes": Quote.objects.all(),
    }
    return render(request,'quote_app/quote.html',context)

def addquote(request):
    if request.method == "POST":
        errors = Quote.objects.quote_validator(request.POST)
        if len(errors): # checking for errors
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ("/quotes")
        getuser = User.objects.get(id=request.session['user_id'])
        Quote.objects.create(author=request.POST['author'], quote=request.POST['quote'], user=getuser)
    return redirect('/quotes')

def userquotes(request,id):

    user = User.objects.get(id=id)

    context = {
        "quotes":Quote.objects.filter(user=user),  
        "this_user":User.objects.get(id=id) 
    }

    return render(request, 'quote_app/quotes_display.html',context)

def account(request,id):
    context = {
        "user" : User.objects.get(id=id),
    }
    return render(request,'quote_app/profile.html',context)

def editaccount(request,id):
    if request.method == "POST":
        errors = User.objects.editprofile_validator(request.POST)
        if len(errors): # checking for errors
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ('/myaccount/' + id)
        edit = User.objects.get(id=id)
        edit.first_name = request.POST['first_name']
        edit.last_name = request.POST['last_name']
        edit.email = request.POST['email']
        edit.save()
        request.session['first_name'] = request.POST['first_name']
        request.session['last_name'] = request.POST['last_name']
        request.session['email'] = request.POST['email']
        id = str(edit.id)
    return redirect('/quotes')

def back(request):
    return redirect('/quotes')

def like(request,id):
    user = User.objects.get(id=request.session['user_id'])
    quote = Quote.objects.get(id=id)
    quote.like.add(user)
    quote.save()
    return redirect('/quotes')

def delete(request,id):
    currentquote = Quote.objects.get(id=id)
    currentquote.delete()
    return redirect('/quotes')