#https://www.youtube.com/watch?v=PUMMCLrVn8A

import pandas as pd
from tqdm.notebook import tqdm
import snscrape.modules.twitter as sntwitter
from stopWordz import stopWords

def TweetFilter(tweet): #make the tweet a lowered copy as algorithm assumes the tweet is lowered but keep caps as it expresses stuff
    tweet = tweet.lower().split(' ')
    i = 0
    while i < len(tweet):
        try:
            if list(tweet[i])[-1] == '.':
                tweet[i] = ''.join(list(tweet)[0:-2])
            if "'" in tweet[i] or list(tweet[i])[0] == '#' or list(tweet[i])[0] == '@' or ('http' in tweet[i] and '://' in tweet[i]):
                tweet.remove(tweet[i])
            else:
                i+=1
        except:
            pass
    for word in stopWords:
        for tword in tweet:
            if not tweet:
                return tweet
            if tword == word:
                tweet.remove(tword)
    return tweet




scraper_objct = sntwitter.TwitterSearchScraper("#trump")

i = 0
for tweet in scraper_objct.get_items():
    print(tweet.rawContent)
    print(TweetFilter(tweet.rawContent))
    print('------------------------------')
    i+=1
    if i > 50:
        print('hmm')
        exit()


    