import tweepy
import time
import pywintypes
from win10toast import ToastNotifier



def main():
    
    period=30
    count=2
    
    toast=ToastNotifier()
    toast.show_toast('Twitter Bot',f'Bot will retweet {count} tweets in every {period} min!!',duration=30)
    
    auth=0
    while(auth==0):
        
        try:
            auth_details=tweepy.OAuthHandler("GnfAM5f1z3wHDW3advJ5YobUg","vfKyH19lAOZVMEicv2UqPoHFhdmdJQdQGigQXKGa4PaAo2avhm")
            auth_details.set_access_token("1361612620806033413-7aRH9mX7qc7LUp9xkcf8XEyA8r705a","iTfMaLOPHgtGRz7KpuMybHBtFah5Ap3sjOZNrLt2xWaEB")
    
            api=tweepy.API(auth_details,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
            auth=1
            
        except Exception as e:
            print(e)

    query=['#gamedev','#indiedev']
    
    while(True):
        
        for i in range(30*60):
            print(i,end='\r')
            time.sleep(1)
        
        print('start collecting tweets ....')
        path='E:/final-project/twitter-bot/index'
        with open(path,'r') as f:
            last_index=f.read()
        
        
        list_tweets=list(api.search(q=query,max_id=last_index,count=100))
        
        tweets=[]
        for tweet in list_tweets:
            if(tweet._json['user']['followers_count']<=200 and not tweet._json['retweeted']):
                tweets.append(tweet._json['id'])
        
        print(f'retweeting {count} tweets')
        tweets=list(set(tweets))

        # for tweet in tweets:
        #     try:
        #         api.retweet(tweet)
        #         print(tweet)
        #     except tweepy.TweepError:
        #         print('skip')
        
        i=0
        for tweet in tweets:
            
            try:
                api.retweet(tweet)
                i+=1
                print(i,tweet)
                last_index=tweet
                if(i==count):
                    break
            except Exception as e:
                print(e)
        
        with open(path,'w') as f:
            f.write(str(last_index))
        
        
if __name__=='__main__':
    main()

