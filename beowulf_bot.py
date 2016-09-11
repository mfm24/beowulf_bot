import markovify
import requests
import tweepy
import json
import os

bw = open('beowulf.txt').read()

m = markovify.Text(bw)

secrets = json.load(open('hrothgar_secrets.json'))
auth = tweepy.OAuthHandler(secrets['API Key'], secrets['API Secret'])
auth.secure = True
auth.set_access_token(secrets['Access Token'], secrets['Access Token Secret'])
t = tweepy.API(auth)

for __ in range(10):
    tweet = m.make_sentence()
    print("Tweeting: ", tweet)
    try:
        t.update_status(tweet)
        break
    except tweepy.error.TweepError:
        pass
