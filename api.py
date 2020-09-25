import pandas as pd   
import requests  
import time    
import datetime
import os

print('Starting up data mining machine to make calls to the pushshift.io reddit API')


def push_shift_api_call(subreddit_name):
    time.sleep(15)
    entries = []
    if os.path.isfile(f'./{subreddit_name}.csv') == True:
        csv = pd.read_csv(f'./{subreddit_name}.csv')
        if csv.created_utc.min() > 1:
            before = f'&before={csv.created_utc.min()}'
    else:
        before= ""
    url = f'https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit_name}{before}&size=100'
    r = requests.get(url)   #this is the actual request, the r is a convention to pull data that's not processed
    data = r.json()
    post = [i['body'] for i in data['data'] if 'distinguished' not in i.keys() and i['author'] != '[deleted]']
    author = [i['author'] for i in data['data'] if 'distinguished' not in i.keys() and i['author'] != '[deleted]']
    created_utc = [i['created_utc'] for i in data['data'] if 'distinguished' not in i.keys() and i['author'] != '[deleted]']
    subreddit = [i['subreddit'] for i in data['data'] if 'distinguished' not in i.keys() and i['author'] != '[deleted]']
    for j in range(len(post)):
        entries.append({'author':author[j],
                     'created_utc':created_utc[j],
                     'post':post[j],
                     'subreddit':subreddit[j]
                     })
    df = pd.DataFrame(entries)
    if os.path.isfile(f'./{subreddit_name}.csv') != True:
        df.to_csv(f'./{subreddit_name}.csv', index=False)
    else:
        df.to_csv(f'./{subreddit_name}.csv', mode='a', header=False, index=False)
    print(f'{df.shape[0]} entries pulled from {subreddit_name} subreddit and added to {subreddit_name}.csv')
    time.sleep(15)


rick_astley_is_never_gonna_give_you_up = True
while rick_astley_is_never_gonna_give_you_up == True:
    push_shift_api_call('conspiracy')
    time.sleep(15)
    push_shift_api_call('news')
    time.sleep(15)