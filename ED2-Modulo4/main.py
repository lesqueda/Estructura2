import tweepy
import json

#4 cadenas para la autenticación
consumer_key = 
consumer_secret = 
access_token = 
access_token_secret = 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,
wait_on_rate_limit_notify=True)

# Obtener followers de un usuario utilizando paginación
#for user in tweepy.Cursor(api.followers, screen_name="nike").items(100):
 #   print (json.dumps(user._json, indent=2))

# Obtener followees de un usuario utilizando paginación
#for user in tweepy.Cursor(api.friends, screen_name="nike").items(5):
#    print (json.dumps(user._json, indent=2))

# obtener un timeline
#for tweet in tweepy.Cursor(api.user_timeline, screen_name="nike", tweepy_mode="extended").items(1):
#    print (json.dumps(tweet._json, indent=2))

#Como buscar tweets
keyword = input("Introduce la keyword: ")
# try:
#     for tweet in tweepy.Cursor(api.search, q=keyword, tweepy_mode="extended").items(10):
#         print (json.dumps(tweet._json, indent=2))
# except:
#     print ("Nothing to return")


for tweet in tweepy.Cursor(api.search, q=keyword, tweet_mode="extended").items(10):
    print (tweet._json["full_text"])
