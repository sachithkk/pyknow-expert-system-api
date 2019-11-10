from pyknow  import *
import logging as logger
from flask_pymongo import PyMongo

from app import flaskAppInstance


class Laptop(Fact):
    pass;


class LaptopService(KnowledgeEngine):
    # def __init__(self, a):
    #     self.a = a
    #     logger.info("This is model name : "+ self.a)

    laptop_model_point = {}

    #
    # connect with mongo database
    #
    flaskAppInstance.config['MONGO_DBNAME'] = 'techRingdb'
    flaskAppInstance.config['MONGO_URI'] = 'mongodb://localhost:27017/techRingdb'
    mongo = PyMongo(flaskAppInstance)

    #result = mongo.db.cpu_mode_point.find();
    # result = mongo.db.x.find();

    # variable point
    compational_power_point = 0

    @DefFacts()
    def __const__(self):
        logger.info("Called Defacts method.")
        yield Fact(laptop_init=True)



    #
    # CPU type point calculation.
    #

    @Rule(Laptop(cpuModel="core i3"))
    def cpu_model_1(self):
    
        result = self.mongo.db.cpu_mode_point.find_one({"model": "core i3"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info("Laptop Model ")

    @Rule(Laptop(cpuModel="core i5"))
    def cpu_model_2(self):
    
        result = self.mongo.db.cpu_mode_point.find_one({"model": "core i5"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info("Laptop Model ")

    @Rule(Laptop(cpuModel="core i7"))
    def cpu_model_3(self):
    
        result = self.mongo.db.cpu_mode_point.find_one({"model": "core i7"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info("Laptop Model ")

    @Rule(Laptop(cpuModel="core i9"))
    def cpu_model_4(self):
    
        result = self.mongo.db.cpu_mode_point.find_one({"model": "core i9"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info("Laptop Model ")

    #
    # CPU core point calculation.
    #

    @Rule(Laptop(cpuCoresSize="2"))
    def cpu_core_1(self):
    
        result = self.mongo.db.cpu_core_point.find_one({"size": "2"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Cores Size ")

    @Rule(Laptop(cpuCoresSize="4"))
    def cpu_core_2(self):
    
        result = self.mongo.db.cpu_core_point.find_one({"size": "4"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Cores Size ")

    @Rule(Laptop(cpuCoresSize="6"))
    def cpu_core_3(self):
    
        result = self.mongo.db.cpu_core_point.find_one({"size": "6"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Cores Size ")

    @Rule(Laptop(cpuCoresSize="8"))
    def cpu_core_4(self):
    
        result = self.mongo.db.cpu_core_point.find_one({"size": "8"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Cores Size ")

    @Rule(Laptop(cpuCoresSize="10"))
    def cpu_core_5(self):
    
        result = self.mongo.db.cpu_core_point.find_one({"size": "10"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Cores Size ")

    @Rule(Laptop(cpuCoresSize="12"))
    def cpu_core_6(self):
    
        result = self.mongo.db.cpu_core_point.find_one({"size": "12"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Cores Size ")

    #
    # CPU cache point calculation.
    #

    @Rule(Laptop(cpuCachSize="3"))
    def cpu_cache_1(self):
    
        result = self.mongo.db.cpu_catch_point.find_one({"size": "3"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Cash Size ")

    @Rule(Laptop(cpuCachSize="4"))
    def cpu_cache_2(self):
    
        result = self.mongo.db.cpu_catch_point.find_one({"size": "4"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Cash Size ")

    @Rule(Laptop(cpuCachSize="6"))
    def cpu_cache_3(self):
    
        result = self.mongo.db.cpu_catch_point.find_one({"size": "6"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Cash Size ")

    @Rule(Laptop(cpuCachSize="8"))
    def cpu_cache_4(self):
    
        result = self.mongo.db.cpu_catch_point.find_one({"size": "8"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Cash Size ")

    @Rule(Laptop(cpuCachSize="9"))
    def cpu_cache_5(self):
    
        result = self.mongo.db.cpu_catch_point.find_one({"size": "9"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Cash Size ")

    #
    # RAM type point calculation.
    #

    @Rule(Laptop(ramType="DDR3"))
    def ram_type_1(self):
    
        result = self.mongo.db.cpu_ram_point.find_one({"type": "DDR3"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Ram Type ")

    @Rule(Laptop(ramType="DDR4"))
    def ram_type_2(self):
    
        result = self.mongo.db.cpu_ram_point.find_one({"type": "DDR4"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Ram Type ")

    #
    # RAM size point calculation.
    #

    @Rule(Laptop(ramSize="2 GB"))
    def ram_size_1(self):
    
        result = self.mongo.db.cpu_ram_size_point.find_one({"size": "2 GB"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Ram Size ")

    @Rule(Laptop(ramSize="4 GB"))
    def ram_size_2(self):
    
        result = self.mongo.db.cpu_ram_size_point.find_one({"size": "4 GB"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Ram Size ")

    @Rule(Laptop(ramSize="6 GB"))
    def ram_size_3(self):
    
        result = self.mongo.db.cpu_ram_size_point.find_one({"size": "6 GB"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Ram Size ")

    @Rule(Laptop(ramSize="8 GB"))
    def ram_size_4(self):
    
        result = self.mongo.db.cpu_ram_size_point.find_one({"size": "8 GB"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Ram Size ")
        
    @Rule(Laptop(ramSize="12 GB"))
    def ram_size_5(self):
    
        result = self.mongo.db.cpu_ram_size_point.find_one({"size": "12 GB"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Ram Size ")

    @Rule(Laptop(ramSize="16 GB"))
    def ram_size_6(self):
    
        result = self.mongo.db.cpu_ram_size_point.find_one({"size": "16 GB"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Ram Size ")

    #
    # STORAGE type point calculation.
    #

    @Rule(Laptop(storageType="HDD"))
    def storage_type_1(self):
    
        result = self.mongo.db.cpu_storage_type_point.find_one({"type": "HDD"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Storage Type ")

    @Rule(Laptop(storageType="SSD"))
    def storage_type_2(self):
    
        result = self.mongo.db.cpu_storage_type_point.find_one({"type": "SSD"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Storage Type ")

    #
    # STORAGE size point calculation.
    #

    @Rule(Laptop(storageSize="128 GB"))
    def storage_size_1(self):
    
        result = self.mongo.db.cpu_storage_size_point.find_one({"size": "128 GB"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Storage Size ")

    @Rule(Laptop(storageSize="256 GB"))
    def storage_size_2(self):
        result = self.mongo.db.cpu_storage_size_point.find_one({"size": "256 GB"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Storage Size ")

    @Rule(Laptop(storageSize="512 GB"))
    def storage_size_3(self):
        result = self.mongo.db.cpu_storage_size_point.find_one({"size": "512 GB"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Storage Size ")

    @Rule(Laptop(storageSize="1000 GB"))
    def storage_size_4(self):
        result = self.mongo.db.cpu_storage_size_point.find_one({"size": "1000 GB"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Storage Size ")

    #
    # BATTERY type point
    #

    @Rule(Laptop(batteryType="Li-Pol"))
    def battery_type_1(self):
        result = self.mongo.db.cpu_battery_type_point.find_one({"type": "Li-Pol"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Battery Size ")

    @Rule(Laptop(batteryType="Li-Ion"))
    def battery_type_2(self):
        result = self.mongo.db.cpu_battery_type_point.find_one({"type": "Li-Ion"})
        self.compational_power_point = self.compational_power_point + result["point"]
        
        logger.info(self.compational_power_point)
        logger.info("Battery Size ")

    logger.info(compational_power_point);

    def result(self):
        return self.compational_power_point;
