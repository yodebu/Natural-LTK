#!usr/bin/env python2
 
'''

@author : Debapriya Das
@date : 11 - 06 - 2015
@Description : Uses the STREAM API of twitter and the Tweepy Library to scrape tweets for different specified keywords as JSON


'''
 



import io
import simplejson as json
import twitter
 
# Go to https://apps.twitter.com/ to create an app and get values for these credentials    
#Variables that contains the user credentials to access Twitter API 
CONSUMER_KEY = '3DQQnOqSU49NaEqmdlNpq2dkP'
CONSUMER_SECRET ='HY2rMdXzMrWF6RS9X4xbs3MEg38Gp9Q0b4I2MtOw7F420SB2zV'
OAUTH_TOKEN = '214098626-6aFra9VcTKEjDQvVfSADDNMeJLjLYmZs10dKvoKp'
OAUTH_TOKEN_SECRET = 'TPnqVOVLNuT36YvB0NEujcsIqGNaSFYeHOSlfG7Dx3U24'

 
# Authenticate with OAuth    
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)
    
# Create a connection to the Twitter Streaming API
twitter_stream = twitter.TwitterStream(auth=auth)
 
QUERY = 'wwdc'
OUT_FILE = 'tweets_'+QUERY+'.json'
 
print 'Filtering the public timeline for "{0}"'.format(QUERY)
 
stream = twitter_stream.statuses.filter(track=QUERY)
 
# Write one tweet per line as a JSON document. 
with io.open(OUT_FILE, 'a', encoding='utf-8',buffering=1) as f:
    for tweet in stream:
        f.write(unicode(u'{0}\n'.format(json.dumps(tweet, ensure_ascii=False))))
        print tweet['text']
