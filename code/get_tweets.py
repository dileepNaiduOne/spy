import tweepy
import time
import os
from dotenv import load_dotenv
load_dotenv()


# Replace with your own API credentials
api_key = os.getenv("0_API_Key")
api_key_secret = os.getenv("0_API_Key_Secret")
access_token = os.getenv("0_Access_Token")
access_token_secret = os.getenv("0_Access_Token_Secret")
bearer_token = os.getenv("0_Bearer_Token")

def get_tweets(number, username):
    client = tweepy.Client(bearer_token)

    # Get user ID from username
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


if __name__ == "__main__":
   tweets = get_tweets(number=5, username="RGVzoomin")

   for tweet in tweets:
       print(tweet.text)

''' 
    ######################
    ##      OUTPUT      ##
    ######################
    User ID for RGVzoomin: 43017766
    Total tweets fetched: 9
    Error getting tweets: 429 Too Many Requests
    Too Many Requests

    1 --> Hi @UrmilaMatondkar ,
    Director Ridley scott on the 30 th anniversary of his film ALIEN said that if u see ur own film after many many years , u might actually wonder if u urself made that film 

    I felt that in parts when watching Satya yesterday and I also was discovering so many… https://t.co/mqRersuMcj
    
    2 --> Hey #JDChekri When I saw the film last night I realised that u did not play a character, but u played an emotion
    What struck me most about your performance was the quiet intensity laced with intelligence . 
    U played a man of few words, someone who carried the weight of some… https://t.co/G3yDYPXdRU
    
    3 --> Hey @BajpayeeManoj after seeing SATYA after so many years I discovered so many new things .. You didn’t just play Bhiku — you became him and breathed life into a role that redefined the way one viewed cinematic characters at that time  . Ur raw and magnetic portrayal elevated… https://t.co/C3GiwyzjKi
    
    4 --> The REUNION of the ENTIRE CAST of SATYA @UrmilaMatondkar @BajpayeeManoj #JDCHEKRI , #VishalBharadwaj @anuragkashyap72 #MakrandDeshpande on the ocassiom of the RE RELEASE of SATYA tmrw the 17 th https://t.co/CEYl7ENiyJ
    
    5 --> Me and SATYA on our way to see SATYA https://t.co/0jDA0sphYa
    
    6 --> Thrilled to be meeting the entire team of SATYA in Mumbai for a pre release event tmrw the 15 th attended by #JDChekri @BajpayeeManoj @UrmilaMatondkar #SaurabhShukla #MakrandDeshpande @AnuragKashyap72 #ShefaliShah and #SandeepChowta ..Film releasing 17 th
    
    7 --> I loved PUSHPA 2 but now after seeing G C I want to fall on the feet of @alluarjun and @SukumarWritings 🙏🙏🙏
    
    8 --> If G C costed some 450 cr then RRR in its extraordinary never before seen visual appeal should have costed 4500 cr and if G C film’s first day collections are 186 cr on day 1 , then PUSHPA 2 collections should have been 1,860 cr ..The point is that the fundamental requirement of… https://t.co/u7SbvX2L8B
    
    9 --> If @ssrajamouli and @SukumarWritings sky rocketed telugu cinema in real time collections into a fantastically stratospheric heights thereby sending legitimate shock waves into Bollywood, the people behind G C succeeded in proving that the south is much more FANTASTIC in being a… https://t.co/zTpGCVjpKD
'''