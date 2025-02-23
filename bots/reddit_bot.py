# reddit_bot.py
import praw
import os

reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent="Neural-dsl Bot by /u/Lemniscate-SHA-256"
)

def post_release(version):
    subreddit = reddit.subreddit("learnmachinelearning")
    title = f"Neural-dsl v{version} Released—10 Bug Fixes, Feedback Welcome!"
    body = f"Hi, I’m a beginner coder improving Neural-dsl, a DSL for neural networks. v{version} fixes 10 bugs (e.g., dashboard visuals). Try `pip install neural-dsl=={version}`. GitHub: [link]. Feedback?"
    subreddit.submit(title, selftext=body)