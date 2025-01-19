import tweepy
import praw
import time
import os
from dotenv import load_dotenv
load_dotenv()

class Get_Data():

    #############################
    #---Get Data From Twitter---#
    #############################
    def get_tweets(self, number, username):
        # api_key = os.getenv("0_API_Key")
        # api_key_secret = os.getenv("0_API_Key_Secret")
        # access_token = os.getenv("0_Access_Token")
        # access_token_secret = os.getenv("0_Access_Token_Secret")
        bearer_token = os.getenv("0_Bearer_Token")

        client = tweepy.Client(bearer_token)

        try:
            user = client.get_user(username=username)
            user_id = user.data.id
            print(f"User ID for {username}: {user_id}")
        except Exception as e:
            print(f"Error getting user ID for {username}: {e}")
            return []

        all_tweets = []
        next_token = None
        
        while True:
            try:
                response = client.get_users_tweets(
                    id=user_id,
                    max_results=number,
                    pagination_token=next_token,
                    tweet_fields=["created_at", "text", "author_id"]
                )

                if response.data:
                    all_tweets.extend(response.data)
                    print(f"Total tweets fetched: {len(all_tweets)}")
                
                next_token = response.meta.get('next_token')
                if not next_token:
                    break
            except Exception as e:
                print(f"Error getting tweets: {e}")
                break
            
            time.sleep(1)

        return all_tweets
    

    ############################
    #---Get Data From Reddit---#
    ############################
    def get_reddits(self, username):
        api_key = os.getenv("0_reddit_api_key")
        api_secret = os.getenv("0_reddit_api_secret")
        user_agent = os.getenv("0_reddit_user_agent")

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
    reddit_human = Get_Data()
    posts = reddit_human.get_reddits(username="AgentCausative")

    for post in posts:
        print("Title:", post["title"])
        print("Text:", post["text"])
        print("URL:", post["url"])
        print("Created Time:", time.ctime(post["created_utc"]))
        print("----")