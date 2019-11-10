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

        logger.info(requestData['cpuModel'])
        logger.info(requestData['cpuCoresSize'])
        logger.info(requestData['cpuCachSize'])
        logger.info(requestData['cpuBoostSpeed'])
        logger.info(requestData['ramType'])
        logger.info(requestData['ramSize'])
        logger.info(requestData['storageType'])
        logger.info(requestData['storageSize'])
        logger.info(requestData['batteryType'])
        logger.info(requestData['batteryCapacity'])
        logger.info(requestData['gpuMemorySize'])
        logger.info(requestData['gpuBooStSpeed'])

        logger.info("****")
        logger.info("****")

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
        result = laptopservice.result();

        print(result);

        return jsonify({"point": result})
