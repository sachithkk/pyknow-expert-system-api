from flask_restful import Resource
from flask import jsonify, request
import logging as logger
from app import flaskAppInstance
from flask_pymongo import PyMongo

import re, sys , pymongo, time, requests, os.path, csv
from selenium import webdriver


class CommentsController(Resource):

    def post(self):
        logger.info("Starting Scrape Comments....")

        requestData = request.get_json()

        # get relative path
        my_path = os.path.abspath(os.path.dirname(__file__))
        chrome_path = os.path.join(my_path, "..\chromeDriver\chromedriver.exe")

        # without headless mode
        # driver = webdriver.Chrome(chrome_path)

        # run hedless mode
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(chrome_path, options=chrome_options)

        # # hide browser
        # driver.set_window_position(-10000,0)

        # get steam site
        driver.get("https://www.youtube.com/")
        driver.maximize_window()

        # get game name by command-line argument
        # search_tag = sys.argv[1]

        search_tag = requestData["product_name"]

        # search the video
        search_video = driver.find_element_by_name("search_query")
        search_video.send_keys(search_tag)
        search_video.submit()

        # #  click filters
        # driver.find_element_by_xpath("""//*[@id="container"]/ytd-toggle-button-renderer""").click()

        # get first video
        driver.find_element_by_xpath("""//*[@id="thumbnail"]/yt-img-shadow""").click()

        # driver.find_element_by_tag_name("yt-formatted-string").click()
        #

        # -----------------------------------------------------------------------------------

        time.sleep(4)
        driver.find_element_by_class_name("ytp-mute-button").click()
        driver.find_element_by_class_name("ytp-play-button").click()

        comment_section = driver.find_element_by_xpath('//*[@id="comments"]')
        driver.execute_script("arguments[0].scrollIntoView();", comment_section)
        time.sleep(7)

        last_height = driver.execute_script("return document.documentElement.scrollHeight")
        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

            # Wait to load page
            time.sleep(2)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.documentElement.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

        # create CSV file
        with open('C:/Users/Sachith/PycharmProjects/tech-ring-py-api/data/comments.csv', 'w', encoding='utf-8', newline='') as file:
            fieldNames = ['username', 'comment']
            theWriter = csv.DictWriter(file, fieldnames=fieldNames)
            theWriter.writeheader()

            time.sleep(3)
            name_elems = driver.find_elements_by_xpath('//*[@id="author-text"]')
            comment_elems = driver.find_elements_by_xpath('//*[@id="content-text"]')
            num_of_names = len(name_elems)
            for i in range(num_of_names):
                username = name_elems[i].text  # .replace(",", "|")
                comment = comment_elems[i].text  # .replace(",", "|")

                # write to CSV file
                theWriter.writerow({'username': username, 'comment': comment})

        # Wait analyze comments
        time.sleep(2)

        # exit the current tab
        driver.__exit__()

        #  Analyze comments
        import nltk
        import pandas as pd
        import warnings

        # nltk.download('vader_lexicon')

        from nltk.sentiment.vader import SentimentIntensityAnalyzer
        sid = SentimentIntensityAnalyzer()

        warnings.filterwarnings("ignore")

        # read the CSV file
        df = pd.read_csv('C:/Users/Sachith/PycharmProjects/tech-ring-py-api/data/comments.csv')

        df.dropna(inplace=True)

        df['scores'] = df['comment'].apply(lambda message: sid.polarity_scores(message))

        from nltk.sentiment.vader import SentimentIntensityAnalyzer
        sid = SentimentIntensityAnalyzer()

        df['score'] = df['comment'].apply(lambda comment: sid.polarity_scores(comment))
        df['compound'] = df['scores'].apply(lambda d: d['compound'])
        df['comp_score'] = df['compound'].apply(lambda score: 'pos' if score >= 0 else 'neg')
        df['compound'] = df['scores'].apply(lambda d: d['compound'])

        sum_compound = df['compound'].sum()
        count = df['compound'].count()

        print(sum_compound)
        print(count)

        avarage_compound = sum_compound / count;
        print("Avarage Compound Value : ", avarage_compound)

        if (avarage_compound >= 0):
            print("Positive Feedback")
        else:
            print("Negative Feedback")

        return jsonify({"avg_compound_value": avarage_compound})