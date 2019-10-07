from flask_restful import Resource
from flask import jsonify, request
import logging as logger

from app import flaskAppInstance
from pymongo import MongoClient

class BuildForPriceController(Resource):

    def post(self):
        logger.info("Starting build for price controller")
        requestData = request.get_json()

        #
        # connect with mongo database
        #
        client = MongoClient('mongodb://localhost:27017')
        db = client.techRingdb

        build_arr = []

        price_min = requestData["min"]
        price_max = requestData["max"]

        ram_min = price_min * (10 / 100)
        ram_max = price_max * (10 / 100)
        motherboard_min = price_min * (30 / 100)
        motherboard_max = price_max * (30 / 100)
        vga_min = price_min * (20 / 100)
        vga_max = price_max * (20 / 100)
        cpu_min = price_min * (20 / 100)
        cpu_max = price_max * (20 / 100)
        hard_disk_min = price_min * (20 / 100)
        hard_disk_max = price_max * (20 / 100)

        ram_arr = []
        vga_arr = []
        cpu_arr = []
        motherboard_arr = []
        hard_disk_arr = []

        #
        # check compatibility function
        #
        def check_compatibility(pro_name, pro, arr):
            if pro_name == "cpu":
                if(pro["socket"].lower() in arr["cpu_brand"].lower()) or (arr["cpu_brand"].lower() in pro["socket"].lower()):
                    return True
                else:
                    return False
            elif pro_name == "ram":
                if(arr["type"].lower() in pro["type"].lower()) or (pro["type"].lower() in arr["type"].lower()):
                    return True
                else:
                    return False
            elif pro_name == "vga":
                if(arr["pci_slot"].lower() in pro["slot"].lower()) or (pro["slot"].lower() in arr["pci_slot"].lower()):
                    return True
                else:
                    return False

        #
        # create build sequence
        #
        def build_sequence(motherboard_arr, cpu_arr, ram_arr, vga_arr, hard_disk_arr):
            for m in motherboard_arr:
                for c in cpu_arr:
                    x = check_compatibility("cpu", c, m)
                    if x == True:
                        for r in ram_arr:
                            x = check_compatibility("ram", r, m)
                            if x == True:
                                for v in vga_arr:
                                    x = check_compatibility("vga", v, m)
                                    if x == True:
                                        for h in hard_disk_arr:
                                            res = {"motherboard": m, "cpu": c, "ram": r, "vga": v, "hard_disk": h}
                                            build_arr.append(res)


        motherboard = db.Motherboard
        for record in motherboard.find().sort("points"):
            if motherboard_min <= float(record['price']) and motherboard_max >= float(record["price"]):
                motherboard_arr.append(record)

        cpu = db.CPU
        for record in cpu.find().sort("points"):
            if cpu_min <= float(record['price']) and cpu_max >= float(record["price"]):
                cpu_arr.append(record)

        ram = db.RAM
        for record in ram.find().sort("points"):
            if ram_min <= float(record['price']) and ram_max >= float(record["price"]):
                ram_arr.append(record)

        vga = db.VGA
        for record in vga.find().sort("points"):
            if vga_min <= float(record['price']) and vga_max >= float(record["price"]):
                vga_arr.append(record)

        hard_disk = db.Hard_Disk
        for record in hard_disk.find().sort("points").limit(1):
            if hard_disk_min <= float(record['price']) and hard_disk_max >= float(record['price']):
                hard_disk_arr.append(record)

        build_sequence(motherboard_arr, cpu_arr, ram_arr, vga_arr, hard_disk_arr)

        return jsonify({"res": build_arr})




