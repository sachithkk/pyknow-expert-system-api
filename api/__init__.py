from flask_restful import Api


from app import flaskAppInstance
from .LaptopController import LaptopController

restServer = Api(flaskAppInstance)

restServer.add_resource(LaptopController, "/api-py-techRing/Laptop")