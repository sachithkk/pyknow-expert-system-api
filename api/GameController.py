from flask_restful import Resource
from selenium import webdriver
import logging as logger
from flask import jsonify, request
import re, sys , pymongo, time, requests, os.path


class GameController(Resource):

    def post(self):
        logger.info("Starting Scrape Game System Requirement")

        requestData = request.get_json()

        # get relative path
        my_path = os.path.abspath(os.path.dirname(__file__))
        chrome_path = os.path.join(my_path, "..\chromeDriver\chromedriver.exe")

        # chrome_path =   "..\chromeDriver\chromedriver.exe"

        # without headless mode
        driver = webdriver.Chrome(chrome_path)

        # run hedless mode
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")

        # driver = webdriver.Chrome(chrome_path, options=chrome_options)

        # # hide browser
        # driver.set_window_position(-10000,0)

        # get steam site
        driver.get("https://store.steampowered.com/search")

        # get game name by command-line argument
        # search_tag = sys.argv[1]

        #  games not age check: far cry 4 | far cry 5 | crysis | call of duty 4 | pubg  | Jurassic World Evolution | Tom Clancys Ghost Recon
        #                       Need For Speed | gta v | Tomb Raider | anno | assassins creed origins | Assassins Creed® Odyssey | HITMAN
        #                       Dota 2 |

        #  games  age check: Call of Duty 7: Black Ops | Call of Duty®: Modern Warfare® 3 | Call of Duty®: Infinite Warfare | Watch_Dogs
        #                   |  Rise of the Tomb Raider |
        search_tag = requestData["game"]

        # search the game
        search_game = driver.find_element_by_id("store_nav_search_term")
        search_game.send_keys(search_tag)
        search_game.submit()

        #  click first game in the search results
        driver.find_element_by_xpath("""//*[@id="search_resultsRows"]/a[1]""").click()

        # get age check url
        url = driver.current_url
        print(url)

        if ("agecheck" in url):
            print("Age Checked")
            # driver.find_element_by_xpath("""// *[ @ id = "ageYear"]""").click()
            search_game = driver.find_element_by_id("ageYear")
            search_game.send_keys("2000")
            driver.find_element_by_class_name("btnv6_blue_hoverfade").click()
            time.sleep(5)

        else :
            print("Age Not-Checked")

        # get game image
        image = driver.find_element_by_class_name("game_header_image_full")
        image_url = image.get_attribute("src")
        print(image_url)

        # game name
        game_name_element = driver.find_element_by_class_name("apphub_AppName")
        game_name = game_name_element.text

        # Get minimum system requirements
        try:
            minimum_requirements = driver.find_element_by_xpath("""//ul[contains(.,'Processor: ')]""")
            print(minimum_requirements.text)
            req = minimum_requirements
        except:
          print("Minimum Requirements Not Available")

        print("------------------------------------------------------------------------------------------------------------------------------------------")

        # Get recommended system requirements if exists
        try:
            recommended_requirements = driver.find_element_by_xpath("""//div[@class='game_area_sys_req_rightCol' and ./ul[contains(.,'Processor: ')]]""")
            print(recommended_requirements.text)
            req = recommended_requirements
            recomended_requirements = 0

        except:
          print("Recommended Requirements Not Available")

        print("------------------------------------------------------------------------------------------------------------------------------------------")

        # split the requirements by new line and ":"
        requirement = req.text
        data = re.split(': |\n', requirement)

        # get the indexes of pc parts
        for x in range(len(data)):
          # print(data[x])
          if data[x] == "Processor":
              cpu_index = x+1

          if data[x] == "Memory":
              memory_index = x+1

          if (data[x] == "Video Card" or data[x] == "Graphics"):
              graphics_index = x+1

          if (data[x] == "Hard Disk Space" or data[x] == "Storage" or data[x] == "Hard Drive" or data[x] == "Disk Space"):
              storage_index = x+1


        # cpu
        cpu = data[cpu_index]

        #  memory
        memory = data[memory_index]

        # graphics
        graphics = data[graphics_index]

        # storage
        storage = data[storage_index]


        # exit the current tab
        driver.__exit__()

        game = { "name": game_name,
                 "cpu": cpu,
                 "ram": memory,
                 "graphics": graphics,
                 "storage": storage,
                 "imageSource": image_url
                 }

        print(game)

        # # insert game in to mongoDB
        # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        # database = myclient["techRingdb"]
        # collection = database["games"]
        #
        # x = collection.insert_one(game)

        # insert game to backend
        responce = requests.post("http://localhost:8080/api-techRing/games/create", json=game)

        print(responce.status_code)
        print(responce.json())

        return jsonify(responce.json())


