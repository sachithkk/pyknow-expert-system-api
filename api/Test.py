from flask_restful import Resource
import logging as logger
from pymongo import MongoClient
from flask import jsonify, request
import json
from bson import json_util, ObjectId

class Test(Resource):

    def get(self):
        logger.info("Test controller")
        requestData = request.get_json()

        client = MongoClient('mongodb://localhost:27017')
        db = client.techRingdb

        ram_arr = []
        vga_arr = []
        cpu_arr = []
        motherboard_arr = []
        hard_disk_arr = []

        build_arr = []

        def build_sequence(motherboard_arr, cpu_arr, ram_arr, vga_arr, hard_disk_arr):
            i = 0
            for m in motherboard_arr:
                if i != 3:
                    for c in cpu_arr:
                            for r in ram_arr:
                                    for v in vga_arr:
                                            for h in hard_disk_arr:
                                                res = {"motherboard": m, "cpu": c, "ram": r, "vga": v, "hard_disk": h}
                                                build_arr.append(res)
                                                i=i+1
                else:
                    return

        motherboard = db.Motherboard
        for record in motherboard.find().sort("points"):
            # if motherboard_min <= float(record['price']) and motherboard_max >= float(record["price"]):
                motherboard_arr.append(record)

        cpu = db.CPU
        for record in cpu.find().sort("points"):
            # if cpu_min <= float(record['price']) and cpu_max >= float(record["price"]):
                cpu_arr.append(record)

        ram = db.RAM
        for record in ram.find().sort("points"):
            # if ram_min <= float(record['price']) and ram_max >= float(record["price"]):
                ram_arr.append(record)

        vga = db.VGA
        for record in vga.find().sort("points"):
            # if vga_min <= float(record['price']) and vga_max >= float(record["price"]):
                vga_arr.append(record)

        hard_disk = db.Hard_Disk
        for record in hard_disk.find().sort("points").limit(1):
            # if hard_disk_min <= float(record['price']) and hard_disk_max >= float(record['price']):
                hard_disk_arr.append(record)

        build_sequence(motherboard_arr, cpu_arr, ram_arr, vga_arr, hard_disk_arr)

        my_json = json.loads(json_util.dumps({'res': build_arr}))

        return my_json