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

tweet = m.make_sentence()
print("Tweeting: ", tweet)
#t.update_status(m.make_sentence())
