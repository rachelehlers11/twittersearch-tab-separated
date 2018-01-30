__author__ = 'rachelsuzanneehlers'
from TwitterSearch import *
import re

# searches Twitter for words or a phrase and writes a TSV of
# resulting text, RTs, and favorites



a1 = 'xxx123'
a2 = 'xxx123'
a3 = 'xxx123'
a4 = 'xxx123'

ts = TwitterSearch(consumer_key=a1, consumer_secret = a2, access_token = a3, access_token_secret = a4)
tso = TwitterSearchOrder()
tso.set_include_entities(True)
#tso.set_include_rts(False)

tso.set_keywords(['Cam Newton'])
tweetDict = {}
wordSet = set()

text_file = open("tweetfile.txt", 'w') # open file in write mode

text_file.write('text' + '\t' + '\t' + 'retweets' + '\t' + 'favorites' + '\n') # write headers

try:
    for tweet in ts.search_tweets_iterable(tso):
        txt = tweet['text'] # the content of the tweet
        favorites = tweet['favorite_count'] # number of favorites
        retweets = tweet['retweet_count'] # number of RTs
        tweetid = tweet['id'] # unique ID
        tweetDict[tweetid] = [txt, favorites, retweets]
        words = set(re.findall(r"(\w+)", txt)) & wordSet

        try:
            text_file.write(str(txt) + '\t' + str(retweets) + '\t' + str(favorites) + '\n')
        except UnicodeEncodeError:
            pass
except TwitterSearchException as e: 
    print(e)

text_file.close()