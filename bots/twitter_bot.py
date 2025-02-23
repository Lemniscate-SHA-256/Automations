# twitter_bot.py
import tweepy
import os

auth = tweepy.OAuthHandler(os.environ["TWITTER_API_KEY"], os.environ["TWITTER_API_SECRET"])
auth.set_access_token(os.environ["TWITTER_ACCESS_TOKEN"], os.environ["TWITTER_ACCESS_TOKEN_SECRET"])
api = tweepy.API(auth)

def post_release(version):
    api.update_status(f"Neural-dsl v{version} released! Fixed 10 bugs (e.g., dashboard visuals). Try pip install neural-dsl=={version}. #MachineLearning #Python [GitHub link]")