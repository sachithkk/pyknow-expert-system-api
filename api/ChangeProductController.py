from flask_restful import Resource
from flask import jsonify, request
import logging as logger
from app import flaskAppInstance
from pymongo import MongoClient
import json
from bson import json_util, ObjectId

class ChangeProductController(Resource):

    def post(self):
        logger.info("Change Product controller")
        requestData = request.get_json()

        #
        # connect with mongo database
        #
        client = MongoClient('mongodb://localhost:27017')
        db = client.techRingdb

        want_product = requestData["product"]
        price_min = requestData["min"]
        price_max = requestData["max"]
        motherboard = requestData["motherboard"]
        cpu = requestData["cpu"]
        ram = requestData["ram"]
        vga = requestData["vga"]
        hard_disk = requestData["hard_disk"]

        res = []

        if motherboard != "":
            col_motherboard = db.Motherboard
            motherboard_pro = col_motherboard.find_one({"_id": ObjectId(motherboard)})

        if cpu != "":
            col_cpu = db.CPU
            cpu_pro = col_cpu.find_one({"_id": ObjectId(cpu)})

        if ram != "":
            col_ram = db.RAM
            ram_pro = col_ram.find_one({"_id": ObjectId(ram)})

        if vga != "":
            col_vga = db.VGA
            vga_pro = col_vga.find_one({"_id": ObjectId(vga)})

        if hard_disk != "":
            col_hard_disk = db.Hard_Disk
            hard_disk_pro = col_hard_disk.find_one({"_id": ObjectId(hard_disk)})

        if want_product == "motherboard":
            for col in col_motherboard.find():
                if motherboard_pro["_id"] != col["_id"]:
                    if col["price"]:
                        if float(price_max) >= float(col["price"]) >= float(price_min):
                            if col["socket"] and cpu_pro["socket"] and col["memory_type"] and ram_pro["type"] and col["pci_slot"] and vga_pro["slot"]:
                                if (col["socket"].lower() in cpu_pro["socket"].lower()) or (cpu_pro["socket"].lower() in col["socket"].lower()):
                                    if (col["memory_type"].lower() in ram_pro["type"].lower()) or (ram_pro["type"].lower() in col["memory_type"].lower()):
                                        if col["pci_slot"].lower() in vga_pro["slot"].lower():
                                            res.append(col)
                                            break

        elif want_product == "cpu":
            for col in col_cpu.find():
                if cpu_pro["_id"] != col["_id"]:
                    if col["price"]:
                        if float(price_max) >= float(col["price"]) >= float(price_min):
                            if col["socket"] and motherboard_pro["socket"]:
                                if (col["socket"].lower() in motherboard_pro["socket"].lower()) or (motherboard_pro["cpu_brand"].lower() in col["socket"].lower()):
                                    res.append(col)
                                    break

        elif want_product == "ram":
            for col in col_ram.find():
                if ram_pro["_id"] != col["_id"]:
                    if col["price"]:
                        if float(price_max) >= float(col["price"]) >= float(price_min):
                            if col["type"] and motherboard_pro["memory_type"]:
                                if (col["type"].lower() in motherboard_pro["memory_type"].lower()) or (motherboard_pro["memory_type"].lower() in col["type"].lower()):
                                    res.append(col)
                                    break

        elif want_product == "vga":
            for col in col_vga.find():
                if vga_pro["_id"] != col["_id"]:
                    if col["price"]:
                        if float(price_max) >= float(col["price"]) >= float(price_min):
                            if col["pci_slot"] and vga_pro["slot"]:
                                if (col["pci_slot"].lower() in vga_pro["slot"].lower()) or (vga_pro["slot"].lower() in col["pci_slot"].lower()):
                                    res.append(col)
                                    break

        elif want_product == "hard_disk":
            for col in col_hard_disk.find():
                if hard_disk_pro["_id"] != col["_id"]:
                    if col["price"]:
                        if float(price_max) >= float(col["price"]) >= float(price_min):
                            res.append(col)
                            break

        my_json = json.loads(json_util.dumps({'res': res}))

        return my_json


