from bson import json_util, ObjectId
import re, sys, pymongo, time, requests, json
from Youtube_videos import youtube_search
from Youtube_videos import comments_search

results = []
abc = []
video_dict = {'youID': [], 'title': [], 'pub_date': []}
def grab_videos(keyword, token=None):
    res = youtube_search(keyword, token=token)
    token = res[0]
    videos = res[1]
    for vid in videos:
        try:
            video_dict['youID'].append(vid['id']['videoId'])
            video_dict['title'].append(vid['snippet']['title'])
            res1 = comments_search(vid['id']['videoId'])
            token = res1[0]
            comments = res1[1]
            a = comments['snippet']['topLevelComment']['snippet']['textDisplay']
            results.append(a)
        except Exception as e:
            print(e)
    return token

def extract_youtube():
    token = grab_videos("Nvidia GeForce")
    count = 0
    while token != "last_page" and count<3:
        token = grab_videos("Nvidia GeForce", token=token)
        count = count+1

# extract_youtube()

a = {}
a["comment_name"] = "Viraj LK"
a["comment"] = "This is a good product"
results.append(a)
a["comment_name"] = "Jason Mamoa"
a["comment"] = "Great and fast"
results.append(a)

my_json = json.loads(json_util.dumps({'res': results, 'rating': 4.5}))

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import warnings
import pandas as pd
sid = SentimentIntensityAnalyzer()
warnings.filterwarnings("ignore")
df = pd.array(results)
df.dropna(inplace=True)
for c in results:
    df['scores'] = c['comment'].apply(lambda message: sid.polarity_scores(message))

print(results)