import tweepy
import json

#4 cadenas para la autenticación
consumer_key = "bOoOpwZln9mTPmTz17jQsiGHQ"
consumer_secret = "Zs5zieoyjnOhqTwDhduQlmyFPSKYy49WWgV7GiSDRf4cdbwJtP"
access_token = "934443992577642496-iYQWLHyvqZAALwJ0apdFRm20s99kapP"
access_token_secret = "V11bvMfv7qDhmM7RzVn4GmKSSXnbq8tRjq4uwS2ROrQQn"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,
wait_on_rate_limit_notify=True)


#Obtener mi información
'''data = api.me() #el .me hace que obtenga mi información
print (json.dumps(data._json, indent=2))'''

#Obtener información de otro usuario.
'''data = api.get_user("nike")
print (json.dumps(data._json, indent=2))'''

#Obtener los followers
#data = api.followers(screen_name="nike")
#print (len(data)) #cantidad de data en el arreglo (ver si está paginada)

#for user in data:
 #   print (json.dumps(user._json, indent=2))

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