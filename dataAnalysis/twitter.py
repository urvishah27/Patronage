import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 
import pandas as pd

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

def clean_tweet(tweet): 
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())

def TwitterClient():
    try:  
        auth = OAuthHandler(consumer_key, consumer_secret) 
        auth.set_access_token(access_token, access_token_secret) 
        api = tweepy.API(auth)
        return api
    except: 
        print("Error: Authentication Failed")
        return None
old_dates = ['2019-02-01', '2019-01-31', '2019-01-30']
new_dates= ['2019-02-07', '2019-02-06', '2019-02-05','2019-02-04', '2019-02-03', '2019-02-02']
all_bjp = pd.DataFrame()
bjp_keywords = ['modi', 'Narendra Modi', 'namo', 'abkibarmodisarkar', 'abkibar', 'abkibaar', 'modisarkar', 'bjp','bhartiya janta party', 'janta party', '#abkibar', '#abkibaar', 'abkibaarmodisarkar', '#abkibarmodisarkar', 'mitron']
ncp_keywords = ['rahul gandhi', 'sonia gandhi', 'priyanka gandhi', 'congress', 'ncp', 'national congress party', 'pappu', '#abkibaar400par', 'abkibaar400par', 'jumla', 'joomla']
api = TwitterClient()
count=1
for keyword in ncp_keywords:
    for old_date in old_dates:
        response_tweets = api.search(keyword, count=200, until=old_date)
        tweets = list()
        for t in response_tweets:
            a = dict()
            print(t.user.name)
            a['text'] = t.text[3:]
            a['tweet_id'] = t.id_str
            a['cleaned_text'] = clean_tweet(t.text[3:])
            analysis = TextBlob(a['cleaned_text'])
            if analysis.sentiment.polarity > 0: 
	            a['sentiment'] = 'positive'
            elif analysis.sentiment.polarity == 0: 
	            a['sentiment'] = 'neutral'
            else: 
	            a['sentiment'] = 'negative'
            a['retweets'] = t.retweet_count
            a['created_at'] = t.created_at
            a['user_name'] = t.user.name
            a['user_url'] = 'https://twitter.com/'+str(t.user.screen_name)
            # print(a['user_url'])
            try:
                a['follower_count'] = t.user.followers_count
            except:
                a['follower_count'] = 1
            try:
                a['profile_image'] = t.user.profile_image_url_https
            except:
                a['profile_image'] = None         
            tweets.append(a)    
        all_bjp = pd.concat([all_bjp, pd.DataFrame(tweets)])
        count = count + 1

all_bjp.drop_duplicates('tweet_id', inplace=True)
all_bjp.to_csv('old_ncp_all.csv', index=False)
print(all_bjp.info())
