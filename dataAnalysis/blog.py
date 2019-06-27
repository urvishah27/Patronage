from bs4 import BeautifulSoup
import requests
from textblob import TextBlob
import pandas as pd
url = input("Enter a website to extract the URL's from: ")
r  = requests.get(url)
b=[]
c=[]
data = r.text
soup = BeautifulSoup(data,"lxml")
for link in soup.find_all('a'):
    rel=link.get('rel')
    title=link.get('title')
    b.append(title)
clean=filter(None,b)
print(clean)
for i in clean:
    a=dict()
    str='Go to'
    str1='profile'
    if str in i:
        if str1 not in i:
            print(i)
            a['Title']=i
            analysis = TextBlob(i)
            if analysis.sentiment.polarity > 0:
                a['sentiment'] = 'positive'
            elif analysis.sentiment.polarity == 0:
                a['sentiment'] = 'neutral'
            else:
                a['sentiment'] = 'negative'
            c.append(a)
pd.DataFrame(c).to_csv('bjpblogs4.csv')



#csv.write(i+"\n")
# blog = "blog.csv"
# csv = open(blog, "w")
# columnTitleRow = "title, rel\n"
# csv.write(columnTitleRow)
# for key in b.keys():
# 	name = key
# 	email = dic[key]
# 	row = name + "," + email + "\n"
# 	csv.write(row)
