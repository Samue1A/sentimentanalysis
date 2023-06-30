from stopWordz import stopWords
a = '''Discrimination is now legal according to the illegitimate Supreme Court.  Show the SCROTUS how their new ruling works.  Refuse all Fascist GOP service everywhere!  #SupremeCourt #SupremeCourtDecision #Trump #TrumpIndictment  #Fascism  #GOP #MAGA #Fascism #GOPBetrayedAmerica https://t.co/JiuzCOjFZw
'''

def TweetFilter(tweet): #make the tweet a lowered copy as algorithm assumes the tweet is lowered but keep caps as it expresses stuff
    tweet = tweet.split(' ')
    i = 0
    while i < len(tweet):
        if list(tweet[i])[-1] == '.':
            tweet[i] = ''.join(list(tweet)[0:-2])
        if "'" in tweet[i] or list(tweet[i])[0] == '#' or list(tweet[i])[0] == '@' or ('http' in tweet[i] and '://' in tweet[i]):
            tweet.remove(tweet[i])
        else:
            i+=1
    for word in stopWords:
        for tword in tweet:
            if not tweet:
                return tweet
            if tword == word:
                tweet.remove(tword)
    return tweet
