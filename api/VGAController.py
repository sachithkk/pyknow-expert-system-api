from flask_restful import Resource
from selenium import webdriver
import logging as logger
from flask import jsonify, request
import re, sys , pymongo, time, requests, os.path

from service.RAMServiceImpl import RAMService
from service.RAMServiceImpl import RAM


class VGAController(Resource):

    def post(self):
        logger.info("Starting VGA points calculation")

        requestData = request.get_json()
        vga = requestData["vga"]
        vga = vga.lower()

        # default values
        vga_memory = 1
        vga_model = "ddr 3"


        return jsonify()


