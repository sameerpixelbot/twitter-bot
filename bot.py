import tweepy
import time

def main():
    
    auth_details=tweepy.OAuthHandler("GnfAM5f1z3wHDW3advJ5YobUg","vfKyH19lAOZVMEicv2UqPoHFhdmdJQdQGigQXKGa4PaAo2avhm")
    auth_details.set_access_token("1361612620806033413-7aRH9mX7qc7LUp9xkcf8XEyA8r705a","iTfMaLOPHgtGRz7KpuMybHBtFah5Ap3sjOZNrLt2xWaEB")

    api=tweepy.API(auth_details,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

    query=['#gamedev','#indiedev']
    
    while(True):
        
        time.sleep(30*60)
        path='E:/final-project/twitter-bot/index'
        with open(path,'r') as f:
            last_index=f.read()
        
        
        list_tweets=list(api.search(q=query,max_id=last_index,count=100))
        
        tweets=[]
        for tweet in list_tweets:
            if(tweet._json['user']['followers_count']<=200):
                tweets.append(tweet._json['id'])
        
        tweets=list(set(tweets))
        last_index=tweets[-1]
        for tweet in tweets:
            try:
                api.retweet(tweet)
                print(tweet)
            except tweepy.TweepError:
                print('skip')
        
if __name__=='__main__':
    main()

