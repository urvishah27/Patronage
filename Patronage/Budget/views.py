from django.shortcuts import render
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
import os
MEDIA_URL = '/media/'
import numpy as np
import pandas as pd

def once():
    tweets = pd.read_csv('static/tweet_disp.csv')[1:]
    followers_old = list(str(tweets['follower_count']))
    # followers=[134,44,1,270,2292,797,98,35,43,3]
    followers=[44,1,270,2292,797,98,35,43,3]
    name = list(tweets['user_name'])
    user_url = list(tweets['user_url'])
    image = list(tweets['profile_image'])
    retweets_old = list(tweets['retweets'])
    # retweets = [35253,11112,8173,7437,7143,6385,6353,6219,6176,6119]
    retweets = [11112,8173,7437,7143,6385,6353,6219,6176,6119]
    influence = list(tweets['influence'])
    sentiment = list(tweets['sentiment'])
    sentiment = [x.capitalize() for x in sentiment]
    date = list(tweets['date'])
    full_text = list()
    text= list(tweets['text'])
    for t in text:
        full_text.append(str(t))
    to_send_tweets = zip(followers,name,user_url,image,retweets,influence,sentiment,date,full_text)
    blog=pd.read_csv('static/bjpblogs.csv')
    blog_summary=list(blog.iloc[:,0])
    blog_title=list(blog.iloc[:,1])
    blog_sentiment=list(blog.iloc[:,2])
    blog_href=list(blog.iloc[:,3])
    to_send_blogs = zip(blog_summary, blog_title, blog_sentiment, blog_href)
    return to_send_blogs, to_send_tweets

def index(request):
    to_send_blogs, to_send_tweets = once()
    context={'blogs':to_send_blogs, 'tweets':to_send_tweets}
    return render(request, 'tweets.html', context)

def blog(request):
    to_send_blogs, to_send_tweets = once()
    context={'blogs':to_send_blogs, 'tweets':to_send_tweets}
    return render(request, 'blog.html', context)

def bjpchart(request):
    return render(request, 'bjp-chart.html')  

def ncpchart(request):
    return render(request, 'ncp-chart.html')
      
def mine(request):
    return render(request, 'mine.html')

def bengaluru_bjp(request):
    return render(request, 'bengaluru_bjp.html')

def bengaluru_ncp(request):
    return render(request, 'bengaluru_ncp.html')

def mumbai_bjp(request):
    return render(request, 'mumbai_bjp.html')

def mumbai_ncp(request):
    return render(request, 'mumbai_ncp.html')

def hyderabad_bjp(request):
    return render(request, 'hyderabad_bjp.html')

def hyderabad_ncp(request):
    return render(request, 'hyderabad_ncp.html')

def kolkata_bjp(request):
    return render(request, 'kolkata_bjp.html')  

def kolkata_ncp(request):
    return render(request, 'kolkata_ncp.html')

def delhi_bjp(request):
    return render(request, 'delhi_bjp.html')  

def delhi_ncp(request):
    return render(request, 'delhi_ncp.html')    