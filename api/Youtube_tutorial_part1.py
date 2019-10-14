import sys
from Youtube_videos import youtube_search
import pandas as pd
import json


video_dict = {'youID':[], 'title':[], 'pub_date':[]}

# just_json = test[1]
# len(just_json)


# for video in just_json:
#     print(video['snippet']['title'])

# token = test[0]
# youtube_search("Kingaton Ram", token=token)

video_dict = {'youID': [], 'title': [], 'pub_date': []}
comments = []
def grab_videos(keyword, token=None):
    res = youtube_search(keyword, token=token)
    token = res[0]
    videos = res[1]
    for vid in videos:
        video_dict['youID'].append(vid['id']['videoId'])
        video_dict['title'].append(vid['snippet']['title'])
        comment = vid['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)
        return token

def extract_youtube():
    token = grab_videos("Nvidia GeForce")
    while token != "last_page":
        token = grab_videos("Nvidia GeForce", token=token)

extract_youtube()

print(comments)

