from flask_restful import Api


from app import flaskAppInstance
from .LaptopController import LaptopController
from .CommentsController import CommentsController
from .GameController import GameController
from .ChangeProductController import ChangeProductController
from .PriceController import PriceController
# from .Youtube_videos import youtube_search

restServer = Api(flaskAppInstance)

restServer.add_resource(LaptopController, "/api-py-techRing/Laptop")
restServer.add_resource(CommentsController, "/api-py-techRing/analyze_comments")
restServer.add_resource(GameController, "/api-py-techRing/scrape_game")
restServer.add_resource(ChangeProductController, "/api-py-techRing/change_product")
restServer.add_resource(PriceController, "/api-py-techRing/build_for_price")