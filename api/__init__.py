from flask_restful import Api


from app import flaskAppInstance
from .LaptopController import LaptopController
from .CommentsController  import CommentsController
from .GameController import GameController

restServer = Api(flaskAppInstance)

restServer.add_resource(LaptopController, "/api-py-techRing/Laptop")
restServer.add_resource(CommentsController, "/api-py-techRing/analyze_comments")
restServer.add_resource(GameController, "/api-py-techRing/scrape_game")