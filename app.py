from flask import Flask
import logging as logger
from flask_cors import CORS


logger.basicConfig(level="DEBUG")


flaskAppInstance = Flask(__name__)
cors = CORS(flaskAppInstance, resources={r"*": {"origins": "*"}})

if __name__ == '__main__':
    logger.debug("Starting Application")



    from api import *
    flaskAppInstance.run(host="0.0.0.0" , port=8093 , debug=True , use_reloader=True)