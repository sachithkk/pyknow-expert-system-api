from flask_restful import Resource
import logging as logger
from flask import request
import requests

class DataController(Resource):

    def post(self):
        logger.info("Get data")

        requestData = request.get_json()
        data = requestData["part"]

        if ("cpu" in data ):
            r = requests.get("http://localhost:8080/api-techRing/games/findById/5dc586eaae994c3454d50c81")
            print("//////////////////////////////////////////////////")
            print(r.text)

            parts = [ { "model":"John", "age":30, "city":"New York"},
                     { "name":"John", "age":30, "city":"New York"},
                     { "name":"John", "age":30, "city":"New York"},
                     { "name":"John", "age":30, "city":"New York"},
                     { "name":"John", "age":30, "city":"New York"},
                     { "name":"John", "age":30, "city":"New York"}
                     ]

        if ("ram" in data ):
            parts = "ram"

        if ("vga" in data ):
            parts = "vga"

        if ("motherboard" in data ):
            parts = "motherboard"

        # parts = json.dumps(parts)

        return parts


