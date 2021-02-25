import tweepy
import time
import pywintypes
from win10toast import ToastNotifier

def get_details():
    
    path='specifications.txt'
    with open(path,'r',encoding='utf-8') as f:
        values=f.readlines()

    period=int(values[0].split('=')[1][:-1])
    count=int(values[1].split('=')[1][:-1])
    APIkey=values[2].split('=')[1][:-1]
    APIsecret=values[3].split('=')[1][:-1]
    AUTHtoken=values[4].split('=')[1][:-1]
    AUTHsecret=values[5].split('=')[1][:]
    
    return period,count,APIkey,APIsecret,AUTHtoken,AUTHsecret


def main():
    
    period,count,APIkey,APIsecret,AUTHtoken,AUTHsecret=get_details()
    
    toast=ToastNotifier()
    toast.show_toast('Twitter Bot',f'Bot will retweet {count} tweets in every {period} min!!',duration=30)
    
    auth=0
    while(auth==0):
        
        try:
            auth_details=tweepy.OAuthHandler(APIkey,APIsecret)
            auth_details.set_access_token(AUTHtoken,AUTHsecret)
    
            api=tweepy.API(auth_details,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
            auth=1
            
        except Exception as e:
            print(e)

    query=['#gamedev','#indiedev']
    
    while(True):
        
        for i in range(period):
            print(i,end='\r')
            time.sleep(60)
        
        print('start collecting tweets ....')
        path='index.txt'
        with open(path,'r') as f:
            last_index=f.read()
        
        
        list_tweets=list(api.search(q=query,max_id=last_index,count=100))
        
        tweets=[]
        for tweet in list_tweets:
            if(tweet._json['user']['followers_count']<=200):
                tweets.append(tweet._json['id'])
        
        print(f'retweeting {count} tweets')
        tweets=list(set(tweets))

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


# period,count,APIkey,APIsecret,AUTHtoken,AUTHsecret=get_details()

# auth_details=tweepy.OAuthHandler('GnfAM5f1z3wHDW3advJ5YobUg','vfKyH19lAOZVMEicv2UqPoHFhdmdJQdQGigQXKGa4PaAo2avhm')
# auth_details.set_access_token('1361612620806033413-7aRH9mX7qc7LUp9xkcf8XEyA8r705a','iTfMaLOPHgtGRz7KpuMybHBtFah5Ap3sjOZNrLt2xWaEB')
    
# api=tweepy.API(auth_details,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
# query=['#gamedev','#indiedev']
# last_index=0
# list_tweets=list(api.search(q=query,max_id=last_index,count=100))

# len(AUTHsecret)

# AUTHsecret=='iTfMaLOPHgtGRz7KpuMybHBtFah5Ap3sjOZNrLt2xWaEB'

# print(AUTHsecret)
# print('iTfMaLOPHgtGRz7KpuMybHBtFah5Ap3sjOZNrLt2xWaEB')

# path='specifications.txt'
# with open(path,'r',encoding='utf-8') as f:
#     values=f.readlines()

# values[5].split('=')[1][:]
