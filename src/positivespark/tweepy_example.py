
import tweepy
import os
from datetime import datetime

consumer_key = os.environ.get("API_CONSUMER_KEY")
consumer_secret = os.environ.get("API_CONSUMER_SECRET")
access_token = os.environ.get("API_ACCESS_TOKEN")
access_token_secret = os.environ.get("API_ACCESS_TOKEN_SECRET")

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Create a tweet
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
api.update_status(f"Posted with Tweepy at {dt_string}")
