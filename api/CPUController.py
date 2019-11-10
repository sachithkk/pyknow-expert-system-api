from flask_restful import Resource
from selenium import webdriver
import logging as logger
from flask import jsonify, request
import re, sys , pymongo, time, requests, os.path

from service.CPUServiceImpl import CPUService
from service.CPUServiceImpl import CPU


class CPUController(Resource):

    def post(self):
        logger.info("Starting CPU point calculation")

        requestData = request.get_json()
        cpu = requestData["cpu"]
        cpu = cpu.lower()

        # default values
        cpu_model = "core i3"
        cpu_genaration = "generation 1"
        cpu_speed = 2

        # get 1st cpu if it has more than 1
        if(" or " in cpu):
            data = cpu.split(" or ")
            cpu = data[0]

        if (" / " in cpu):
            data = cpu.split(" / ")
            cpu = data[0]

        if (", " in cpu):
            data = cpu.split(", ")
            cpu = data[0]

        # get cpu model
        if("core i3" in cpu):
            cpu_model = "core i3"

        if ("core i5" in cpu):
            cpu_model = "core i5"

        if ("core i7" in cpu):
            cpu_model = "core i7"

        if ("core i9" in cpu):
            cpu_model = "core i9"

        # get genaration
        if (re.findall(r"1[0-9][0-9][0-9]", cpu)):
            cpu_genaration = "generation 1"

        if (re.findall(r"2[0-9][0-9][0-9]", cpu)):
            cpu_genaration = "generation 2"

        if (re.findall(r"3[0-9][0-9][0-9]", cpu)):
            cpu_genaration = "generation 3"

        if (re.findall(r"4[0-9][0-9][0-9]", cpu)):
            cpu_genaration = "generation 4"

        if (re.findall(r"5[0-9][0-9][0-9]", cpu)):
            cpu_genaration = "generation 5"

        if (re.findall(r"6[0-9][0-9][0-9]", cpu)):
            cpu_genaration = "generation 6"

        if (re.findall(r"7[0-9][0-9][0-9]", cpu)):
            cpu_genaration = "generation 7"

        if (re.findall(r"8[0-9][0-9][0-9]", cpu)):
            cpu_genaration = "generation 8"

        if (re.findall(r"9[0-9][0-9][0-9]", cpu)):
            cpu_genaration = "generation 9"

        # get speed
        if (re.findall(r"1 ghz", cpu) or re.findall(r"1\.[0-9] ghz", cpu) or re.findall(r"1\.[0-9][0-9] ghz", cpu) or re.findall(r"1ghz", cpu) or re.findall(r"1\.[0-9]ghz", cpu) or re.findall(r"1\.[0-9][0-9]ghz", cpu)):
            cpu_speed = 1

        if (re.findall(r"2 ghz", cpu) or re.findall(r"2\.[0-9] ghz", cpu) or re.findall(r"2\.[0-9][0-9] ghz", cpu) or re.findall(r"2ghz", cpu) or re.findall(r"2\.[0-9]ghz", cpu) or re.findall(r"2\.[0-9][0-9]ghz", cpu)):
            cpu_speed = 2

        if (re.findall (r"3 ghz", cpu) or re.findall (r"3\.[0-9] ghz", cpu) or re.findall (r"3\.[0-9][0-9] ghz", cpu) or re.findall (r"3ghz", cpu) or re.findall (r"3\.[0-9]ghz", cpu) or re.findall (r"3\.[0-9][0-9]ghz", cpu)):
            cpu_speed = 3

        if (re.findall (r"4 ghz", cpu) or re.findall (r"4\.[0-9] ghz", cpu) or re.findall (r"4\.[0-9][0-9] ghz", cpu) or re.findall (r"4ghz", cpu) or re.findall (r"4\.[0-9]ghz", cpu) or re.findall (r"4\.[0-9][0-9]ghz", cpu)):
            cpu_speed = 4

        if (re.findall(r"5 ghz", cpu) or re.findall(r"5\.[0-9] ghz", cpu) or re.findall(r"5\.[0-9][0-9] ghz", cpu) or re.findall(r"5ghz", cpu) or re.findall(r"5\.[0-9]ghz", cpu) or re.findall(r"5\.[0-9][0-9]ghz", cpu)):
            cpu_speed = 5

        cpuService = CPUService()
        cpuService.reset()

        cpuService.declare(CPU(cpu_model = cpu_model,
                               cpu_genaration = cpu_genaration,
                               cpu_speed = cpu_speed ))


        cpuService.run()
        r = cpuService.result();

        print(r)

        return jsonify({"cpu points": r })

