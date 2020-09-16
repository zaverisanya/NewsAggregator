from django.shortcuts import render

import requests
from bs4 import BeautifulSoup

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[2:-13] # removing footer links

toi_news=[]
for th in toi_headings:
    toi_news.append(th.text)

ht_r = requests.get("https://inshorts.com/en/read/")
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
ht_headings = ht_soup.findAll("span", {"itemprop": "headline"})
			
ht_headings = ht_headings[1:]
ht_news = []

for hth in ht_headings:
    ht_news.append(hth.text)

p_r = requests.get("https://www.theonion.com/latest")
p_soup = BeautifulSoup(p_r.content, 'html5lib')
p_headings = p_soup.findAll("div", {"class": "cw4lnv-4 eRRMSy"})
			
p_headings = p_headings[1:]
p_news = []

for j in p_headings:
    p_news.append(j.text)
# Create your views here.
def home(req):
    

    return render(req,'news/home.html')
    
def index(req):
    return render(req,'news/index.html')

def toi(req):
    return render(req,'news/toi.html',{'toi_news': toi_news})

def inshorts(req):
    return render(req,'news/inshorts.html',{'ht_news': ht_news})

def ht(req):
    return render(req,'news/ht.html',{'p_news': p_news})

def exit(req):
    return render(req,'news/exit.html')