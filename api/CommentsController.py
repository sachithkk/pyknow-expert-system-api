from flask_restful import Resource
from flask import jsonify, request
import logging as logger
import logging
from bson import json_util, ObjectId
import json
from apiclient.discovery import build


class CommentsController(Resource):

    def post(self):
        logger.info("Starting Scrape Comments....")

        requestData = request.get_json()
        stop_words = {'good video', 'good description', 'nice video', 'thank you for this video'}
        results = []

        def extract_youtube():
            api_key = 'AIzaSyB4klg5itSHIb8Q7JL3CXGJ665b-aTh1o4'
            youtube = build('youtube', 'v3', developerKey=api_key)
            q = requestData["name"]
            q_split = q.split()
            res = True
            rec = 0
            perc_ = 0
            try:
                req = youtube.search().list(q=q_split[0], part='snippet', type='video', maxResults=10)
                res = req.execute()

                for item in res['items']:
                    for c in q_split:
                        if c in item['snippet']['title']:
                            perc_ = perc_ + 1

                    if (perc_ / q_split.__len__()) >= 0.5:
                        req1 = youtube.commentThreads().list(part='snippet', videoId=item['id']['videoId'],
                                                             textFormat="plainText").execute()
                        for a in req1['items']:
                            c = {'comment_name': a["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"],
                                 'comment': a["snippet"]["topLevelComment"]["snippet"]["textDisplay"],
                                 'pro_pic': a["snippet"]["topLevelComment"]["snippet"]["authorProfileImageUrl"]}
                            sentence = a["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
                            for w in stop_words:
                                if w in sentence:
                                    res = False
                                    break
                            if res == True:
                                if rec < 10:
                                    print(sentence)
                                    results.append({"comment_name": a["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"], "comment": sentence})
                                    rec = rec + 1
                                else:
                                    return
                            else:
                                res = True
            except:
                print("error in getting comments from youtube")

        extract_youtube()

        # results = [{"comment_name": "Jason McMillan", "comment": "I have used this man. Itz incrediblly fast. You should try this"},
        #             {"comment_name": "Alberto Sanchez", "comment": "I have used this man. Itz incrediblly fast. You should try this"},
        #             {"comment_name": "Alba Bibin", "comment": "I have used this man. Itz incrediblly fast. You should try this"},
        #             {"comment_name": "Alex Cary", "comment": "I have used this man. Itz incrediblly fast. You should try this"},
        #             {"comment_name": "Gabriel Lasso", "comment": "I have used this man. Itz incrediblly fast. You should try this"},
        #             {"comment_name": "Juan Mackenzie", "comment": "I have used this man. Itz incrediblly fast. You should try this"},
        #             {"comment_name": "Rest Camilo", "comment": "I have used this man. Itz incrediblly fast. You should try this"},
        #             {"comment_name": "Happy Man", "comment": "I have used this man. Itz incrediblly fast. You should try this"},
        #             {"comment_name": "King Slayer", "comment": "I have used this man. Itz incrediblly fast. You should try this"},
        #             {"comment_name": "James Henderson", "comment": "I have used this man. Itz incrediblly fast. You should try this"}]
        my_json = json.loads(json_util.dumps({'res': results}))

        return my_json
