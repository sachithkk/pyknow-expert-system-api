from flask_restful import Resource
from flask import jsonify, request
import logging as logger
from app import flaskAppInstance
from flask_pymongo import PyMongo

from service.LaptopServiceImpl import LaptopService
from service.LaptopServiceImpl import Laptop

class LaptopController(Resource):
    #
    # connect with mongo database
    #
    flaskAppInstance.config['MONGO_DBNAME'] = 'techRingdb'
    flaskAppInstance.config['MONGO_URI'] = 'mongodb://localhost:27017/techRingdb'
    mongo = PyMongo(flaskAppInstance);

    def post(self):

        logger.info("Starting laptop compaire method....")
        requestData = request.get_json()

        cpuModel = requestData['cpuModel']
        cpuCoresSize = requestData['cpuCoresSize']
        cpuCachSize = requestData['cpuCachSize']
        cpuBoostSpeed = requestData['cpuBoostSpeed']
        ramType = requestData['ramType']
        ramSize = requestData['ramSize']
        storageType = requestData['storageType']
        storageSize = requestData['storageSize']
        batteryType = requestData['batteryType']
        batteryCapacity = requestData['batteryCapacity']
        gpuMemorySize = requestData['gpuMemorySize']
        gpuBooStSpeed = requestData['gpuBooStSpeed']

        print("****" + requestData['ramType'])
        print("****" + requestData['ramSize'])

        laptopservice = LaptopService()

        laptopservice.reset()

        laptopservice.declare(Laptop(cpuModel=requestData['cpuModel'],
                                     cpuCoresSize=requestData['cpuCoresSize'],
                                     cpuCachSize=requestData['cpuCachSize'],
                                     ramType=requestData['ramType'],
                                     ramSize=requestData['ramSize'],
                                     storageType=requestData['storageType'],
                                     storageSize=requestData['storageSize'],
                                     batteryType=requestData['batteryType']))

        laptopservice.run()
        r = laptopservice.result();
        print(r);

        return jsonify({"point": r})
