from flask_restful import Resource
import logging as logger
from flask import request
import requests,json

class DataController(Resource):

    def post(self):
        logger.info("Get data")

        requestData = request.get_json()
        data = requestData["part"]

        if ("cpu" in data ):
            r = requests.get("http://localhost:8080/api-techRing/games/findById/5dc586eaae994c3454d50c81")
            print("//////////////////////////////////////////////////")
            print(r.text)

            # parts = [ { "name":"John", "age":30, "city":"New York"},
            #          { "name":"John1", "age":30, "city":"New York"},
            #          { "name":"John2", "age":30, "city":"New York"},
            #          { "name":"John", "age":33, "city":"  York"},
            #          { "name":"John", "age":11, "city":"New  "},
            #          { "name":"John", "age":30, "city":"New York"}
            #          ]
            # parts1 = json.dumps(parts)
            # print(parts1)
            #
            # print(type(parts1))
            #
            # for attrs  in parts1:
            #         print(attrs ['name'])
            #         break
            # else:
            #     print('Nothing found!')


        if ("ram" in data ):
            parts = "ram"

        if ("vga" in data ):
            parts = "vga"

        if ("motherboard" in data ):
            parts = "motherboard"

        # parts = json.dumps(parts)

        return parts


