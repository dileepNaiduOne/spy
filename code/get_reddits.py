import praw
import time
import os
from dotenv import load_dotenv
load_dotenv()

# Reddit API credentials from .env
api_key = os.getenv("0_reddit_api_key")
api_secret = os.getenv("0_reddit_api_secret")
user_agent = os.getenv("0_reddit_user_agent")
username = os.getenv("0_reddit_username")
password = os.getenv("0_reddit_password")


def get_reddits(username):
    reddit = praw.Reddit(
        client_id=api_key,
        client_secret=api_secret,
        user_agent=user_agent
    )

    try:
        user = reddit.redditor(username)

        all_posts = []

        for submission in user.submissions.new(limit=None):
            all_posts.append(
                {
                    "title": submission.title,
                    "text": submission.selftext,
                    "url": submission.url,
                    "created_utc": submission.created_utc,
                }
            )

        return all_posts
    except Exception as e:
        print(f"Error: {e}")
        return []


if __name__ == "__main__":
    posts = get_reddits(username="AgentCausative")

    for post in posts:
        print("Title:", post["title"])
        print("Text:", post["text"])
        print("URL:", post["url"])
        print("Created Time:", time.ctime(post["created_utc"]))
        print("----")