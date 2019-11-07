from flask_restful import Resource
from flask import jsonify, request
import logging as logger
from app import flaskAppInstance
from pymongo import MongoClient
import json
from bson import json_util, ObjectId

class PriceController(Resource):

    def post(self):
        logger.info("Given price controller")
        requestData = request.get_json()

        #
        # connect with mongo database
        #
        client = MongoClient('mongodb://localhost:27017')
        db = client.techRingdb

        ram_min = requestData["ram_min"]
        ram_max = requestData["ram_max"]
        vga_min = requestData["vga_min"]
        vga_max = requestData["vga_max"]
        cpu_min = requestData["cpu_min"]
        cpu_max = requestData["cpu_max"]
        motherboard_min = requestData["motherboard_min"]
        motherboard_max = requestData["motherboard_max"]
        hard_disk_min = requestData["hard_disk_min"]
        hard_disk_max = requestData["hard_disk_max"]

        ram_arr = []
        vga_arr = []
        cpu_arr = []
        motherboard_arr = []
        hard_disk_arr = []

        build_arr = []

        #
        # check compatibility function
        #
        def check_compatibility(pro_name, pro, arr):
            if pro_name == "cpu":
                if pro["socket"] and arr["socket"]:
                    try:
                        if (pro["socket"].lower() in arr["socket"].lower()) or (arr["socket"].lower() in pro["socket"].lower()):
                            return True
                        else:
                            return False
                    except:
                        print("error in cpu compatibility")
                        return False
                else:
                    return False
            elif pro_name == "ram":
                if arr["memory_type"] and pro["type"]:
                    try:
                        if (arr["memory_type"].lower() in pro["type"].lower()) or (pro["type"].lower() in arr["memory_type"].lower()):
                            return True
                        else:
                            return False
                    except:
                        print("error in ram compatibility")
                        return False
                else:
                    return False
            elif pro_name == "vga":
                if arr["pci_slot"] and pro["slot"]:
                    try:
                        if (arr["pci_slot"].lower() in pro["slot"].lower()) or (pro["slot"].lower() in arr["pci_slot"].lower()):
                            return True
                        else:
                            return False
                    except:
                        print("error in vga compatiblity")
                        return False
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
                                            break

        motherboard = db.Motherboard
        for record in motherboard.find().sort("points", -1):
            if record['price']:
                if float(motherboard_min) <= float(record['price']) and float(motherboard_max) >= float(
                        record["price"]):
                    motherboard_arr.append(record)

        cpu = db.CPU
        for record in cpu.find().sort("points", -1):
            if record['price']:
                if float(cpu_min) <= float(record['price']) and float(cpu_max) >= float(record["price"]):
                    cpu_arr.append(record)

        ram = db.RAM
        for record in ram.find().sort("points", -1):
            if record['price']:
                if float(ram_min) <= float(record['price']) and float(ram_max) >= float(record["price"]):
                    ram_arr.append(record)

        vga = db.VGA
        for record in vga.find().sort("points", -1):
            if record['price']:
                if float(vga_min) <= float(record['price']) and float(vga_max) >= float(record["price"]):
                    vga_arr.append(record)

        hard_disk = db.Hard_Disk
        for record in hard_disk.find().sort("points", -1):
            if record['price']:
                if float(hard_disk_min) <= float(record['price']) <= float(hard_disk_max):
                    hard_disk_arr.append(record)
                    break

        build_sequence(motherboard_arr, cpu_arr, ram_arr, vga_arr, hard_disk_arr)

        my_json = json.loads(json_util.dumps({'res': build_arr}))

        return my_json



