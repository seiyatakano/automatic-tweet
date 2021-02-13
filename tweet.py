import tweepy
import time
import numpy as np
import pandas as pd
import re
import datetime


CK='Ow7OUltQgZnufnraoIluGOUOK'
CS='HmwzBK0idCkH5hisPwGf85w6Uia2oBwuwhoJjkHuzeJGO69dVe'
AT='1221050313022615552-JU0mUiurYbOipKFH6IIizbyIku4fFv'
AS='heaBYyxUuEe8tXffsMJVr93BPr7iQ1jp4CkBAor8ME7CN'

# create twitter object
auth=tweepy.OAuthHandler(CK,CS)
auth.set_access_token(AT,AS)
api=tweepy.API(auth)
todayTweetId=[]

def do_tweet():
    pd.set_option('display.max_colwidth', None)
    tweets_df=pd.read_csv('./tweets.csv')
    tweetId=np.random.randint(0, len(tweets_df), 1)
    while tweetId in todayTweetId:
        tweetId=np.random.randint(0,len(tweets_df),1)
    todayTweetId.append(tweetId)
    
    tweet=str(tweets_df.loc[tweetId,'tweets'])
    tweet=re.sub(' ','',tweet)
    for i in range(0,3):
        tweet=re.sub('^[0-9]','',tweet)
    tweet=re.sub('Name:tweets,dtype:object$','',tweet)
    tweet=tweet.replace('\\n','\n')
    api.update_status(tweet)
    
def get_hour():
    now=str(datetime.datetime.now())
    times=re.split('[-:. ]',now)
    nowHour=int(times[3])
    return nowHour

nowHour = get_hour()

if nowHour==6 or nowHour==18 or nowHour==21:
    do_tweet()
elif nowHour==23:
    todayTweetId=[]
