from flask_restful import Resource
from flask import jsonify, request
import logging as logger
from app import flaskAppInstance
from pymongo import MongoClient
from bson import ObjectId

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
        cpu = requestData["motherboard"]
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
                if motherboard != col["_id"]:
                    if float(col["price"]) <= price_max and float(col["price"]) >= price_min:
                        if (col["cpu_brand"].lower() in cpu_pro["socket"].lower()) or (cpu_pro["socket"].lower() in col["cpu_brand"].lower()):
                            if (col["type"].lower() in ram_pro["type"].lower()) or (ram_pro["type"].lower() in col["type"].lower()):
                                if col["pci_slot"].lower() in vga_pro["slot"].lower():
                                    res.append(col)
                                    break

        elif want_product == "cpu":
            for col in col_cpu.find():
                if cpu != col["_id"]:
                    if float(col["price"]) <= price_max and float(col["price"]) >= price_min:
                        if (col["socket"].lower() in motherboard_pro["cpu_brand"].lower()) or (motherboard_pro["cpu_brand"].lower() in col["socket"].lower()):
                            res.append(col)
                            break

        elif want_product == "ram":
            for col in col_ram.find():
                if ram != col["_id"]:
                    if float(col["price"]) <= price_max and float(col["price"]) >= price_min:
                        if (col["type"].lower() in motherboard_pro["type"].lower()) or (motherboard_pro["type"].lower() in col["type"].lower()):
                            res.append(col)
                            break

        elif want_product == "vga":
            for col in col_vga.find():
                if vga != col["_id"]:
                    if float(col["price"]) <= price_max and float(col["price"]) >= price_min:
                        if (col["pci_slot"].lower() in vga_pro["slot"].lower()) or (vga_pro["slot"].lower() in col["pci_slot"].lower()):
                            res.append(col)
                            break

        elif want_product == "hard_disk":
            for col in col_hard_disk.find():
                if hard_disk != col["_id"]:
                    if float(col["price"]) <= price_max and float(col["price"]) >= price_min:
                        res.append(col)
                        break

        return jsonify({"res": res})


