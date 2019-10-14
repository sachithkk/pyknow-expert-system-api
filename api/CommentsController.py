from flask_restful import Resource
from flask import jsonify, request
import logging as logger
from app import flaskAppInstance
from flask_pymongo import PyMongo
import tweepy
import logging
from bson import json_util, ObjectId
import re, sys, pymongo, time, requests, json
import nltk
import pandas as pd
import warnings
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from .Youtube_videos import youtube_search


class CommentsController(Resource):

    def post(self):
        logger.info("Starting Scrape Comments....")

        requestData = request.get_json()

        results = []

        def extract_twiitter():

            consumer_key = "JjOaEAXjUq8b8PVqS1UFQpmur"
            consumer_secret = "Frj1dDqF0nePQr0LYoy2cGhE8s5rmwEgFtkzYWWbJi4f5DBIMA"
            access_token = "1540106498-PQZwiwzWowjjspOIErpc96hAuFKoUj8Pb2TBpLO"
            access_token_secret = "b2viTdZr279qwfAp6LyH6kg4gfU0q7PCzXZpjIJGz2vVX"

            # Creating the authentication object
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            # Setting your access token and secret
            auth.set_access_token(access_token, access_token_secret)
            # Creating the API object while passing in auth information
            api = tweepy.API(auth)

            # The search term you want to find
            query = requestData["name"]
            # Language code (follows ISO 639-1 standards)
            language = "en"

            non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
            try:
                for tweet in tweepy.Cursor(api.search, q=query, count=100, lang="en").items():
                    if "laptop" not in tweet.text:
                        results.append(tweet.text.translate(non_bmp_map))
                        tweet_id = tweet.id
                        user = tweet.user.screen_name
                        for reply in tweepy.Cursor(api.search, q='to:{}'.format(user), since_id=tweet_id, result_type='recent').items(1000):
                            if hasattr(reply, 'in_reply_to_status_id_str'):
                                if reply.in_reply_to_status_id_str == tweet.id_str:
                                    results.append(reply.text.translate(non_bmp_map))
            except:
                print("error1")

        video_dict = {'youID': [], 'title': [], 'pub_date': []}

        def grab_videos(keyword, token=None):
            res = youtube_search(keyword, token=token)
            token = res[0]
            videos = res[1]
            for vid in videos:
                try:
                    video_dict['youID'].append(vid['id']['videoId'])
                    video_dict['title'].append(vid['snippet']['title'])
                    # comment = vid['snippet']['topLevelComment']['snippet']['textDisplay']
                    # results.append(comment)
                except:
                    print("error2")
            return token

        def extract_youtube():
            token = grab_videos(requestData["name"])
            while token != "last_page":
                token = grab_videos(requestData["name"], token=token)

        # extract_twiitter()
        # extract_youtube()

        res = {}
        res['comment_name'] = "Viraj LK"
        res['comment'] = 'Good Product. Highly Recommended'
        results.append(res)
        res = {}
        res['comment_name'] = "John Mason"
        res['comment'] = 'Very fast'
        results.append(res)

        my_json = json.loads(json_util.dumps({'res': results, 'rating': 4.5}))

        return my_json
