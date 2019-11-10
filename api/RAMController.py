from flask_restful import Resource
from selenium import webdriver
import logging as logger
from flask import jsonify, request
import re, sys , pymongo, time, requests, os.path

from service.RAMServiceImpl import RAMService
from service.RAMServiceImpl import RAM


class RAMController(Resource):

    def post(self):
        logger.info("Starting RAM points calculation")

        requestData = request.get_json()
        ram = requestData["ram"]
        ram = ram.lower()

        # default values
        ram_memory = 1
        ram_model = "ddr 3"

        # get ram speed
        if ("1 gb" in ram):
            ram_memory = 1

        if ("2 gb" in ram):
            ram_memory = 2

        if ("3 gb" in ram or "4 gb" in ram):
            ram_memory = 4

        if ("5 gb" in ram or "6 gb" in ram or "7 gb" in ram or "8 gb" in ram):
            ram_memory = 8

        if ("9 gb" in ram or "10 gb" in ram or "11 gb" in ram or "12 gb" in ram or "13 gb" in ram or "14 gb" in ram or "15 gb" in ram or "16 gb" in ram):
            ram_memory = 16

        # get ram model
        if ("ddr 3" in ram or "ddr3" in ram or "ddr-3" in ram):
            ram_model = "ddr 3"

        if ("ddr 4" in ram or "ddr4" in ram or "ddr-4" in ram):
            ram_model = "ddr 4"

        ramService = RAMService()
        ramService.reset()

        ramService.declare(RAM(ram_memory = ram_memory,
                               ram_model = ram_model))


        ramService.run()
        r = ramService.result()

        print(r)

        return jsonify({"ram_points": r})


