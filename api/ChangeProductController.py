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
        type = requestData["type"]

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
            sorted_motherboard = ''
            if type == "quality":
                sorted_motherboard = col_motherboard.find().sort("ratings", -1)
            else:
                sorted_motherboard = col_motherboard.find().sort("price")
            for col in sorted_motherboard:
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
            sorted_cpu = ''
            if type == "quality":
                sorted_cpu = col_cpu.find().sort("ratings", -1)
            else:
                sorted_cpu = col_cpu.find().sort("price")
            for col in sorted_cpu:
                if cpu_pro["_id"] != col["_id"]:
                    if col["price"]:
                        if float(price_max) >= float(col["price"]) >= float(price_min):
                            if col["socket"] and motherboard_pro["socket"]:
                                if (col["socket"].lower() in motherboard_pro["socket"].lower()) or (
                                        motherboard_pro["cpu_brand"].lower() in col["socket"].lower()):
                                    res.append(col)
                                    break

        elif want_product == "ram":
            sorted_ram = ''
            if type == "quality":
                sorted_ram = col_ram.find().sort("ratings", -1)
            else:
                sorted_ram = col_ram.find().sort("price")
            for col in sorted_ram:
                if ram_pro["_id"] != col["_id"]:
                    if col["price"]:
                        if float(price_max) >= float(col["price"]) >= float(price_min):
                            if col["type"] and motherboard_pro["memory_type"]:
                                if (col["type"].lower() in motherboard_pro["memory_type"].lower()) or (
                                        motherboard_pro["memory_type"].lower() in col["type"].lower()):
                                    res.append(col)
                                    break

        elif want_product == "vga":
            sorted_vga = ''
            if type == "quality":
                sorted_vga = col_vga.find().sort("ratings", -1)
            else:
                sorted_vga = col_vga.find().sort("price")
            for col in sorted_vga:
                if vga_pro["_id"] != col["_id"]:
                    if col["price"]:
                        if float(price_max) >= float(col["price"]) >= float(price_min):
                            if vga_pro["slot"]:
                                if col["slot"]:
                                    if (col["slot"].lower() in vga_pro["slot"].lower()) or (
                                            vga_pro["slot"].lower() in col["slot"].lower()):
                                        res.append(col)
                                        break
                            else:
                                res.append(col)

        elif want_product == "hard_disk":
            sorted_hard_disk = ''
            if type == "quality":
                sorted_hard_disk = col_hard_disk.find().sort("ratings", -1)
            else:
                sorted_hard_disk = col_hard_disk.find().sort("price")
            for col in sorted_hard_disk:
                if hard_disk_pro["_id"] != col["_id"]:
                    if col["price"]:
                        if float(price_max) >= float(col["price"]) >= float(price_min):
                            res.append(col)
                            break

        my_json = json.loads(json_util.dumps({'res': res}))
        print(my_json);
        return my_json
