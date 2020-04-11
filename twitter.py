import tweepy
import time

auth = tweepy.OAuthHandler('I','')

auth.set_access_token('','')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'hello'
nrTweets = 10 

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Liked tweet')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break