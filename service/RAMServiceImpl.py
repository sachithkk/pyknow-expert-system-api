from pyknow import *
import logging as logger

from app import flaskAppInstance


class RAM(Fact):
    pass;


class RAMService(KnowledgeEngine):

    ram_total_points = 0

    @DefFacts()
    def __const__(self):
        logger.info("Called Defacts method.")
        # time.sleep(10)
        # self.connect_open()
        yield Fact(ram_init=True)


    #
    # RAM Speed point calculation.
    #
    logger.info("Starting RAM Service")
    @Rule(RAM(ram_speed= "1 gb"))
    def ram_speed_1(self):
        self.ram_total_points = self.ram_total_points + 1
        print("RAM Speed: 1 GB")

    @Rule(RAM(ram_speed= "2 gb"))
    def ram_speed_2(self):
        self.ram_total_points = self.ram_total_points + 2
        print("RAM Speed: 2 GB")

    @Rule(RAM(ram_speed= "4 gb" ))
    def ram_speed_3(self):
        self.ram_total_points = self.ram_total_points + 4
        print("RAM Speed: 4 GB")

    @Rule(RAM(ram_speed= "8 gb" ))
    def ram_speed_4(self):
        self.ram_total_points = self.ram_total_points + 8
        print("RAM Speed: 8 GB")

    @Rule(RAM(ram_speed= "16 gb" ))
    def ram_speed_5(self):
        self.ram_total_points = self.ram_total_points + 16
        print("RAM Speed: 16 GB")

    #
    # RAM Speed point calculation.
    #
    @Rule(RAM(ram_model="ddr 3"))
    def ram_model_1(self):
        self.ram_total_points = self.ram_total_points + 3
        print("RAM Model: DDR 3")

    @Rule(RAM(ram_model="ddr 4"))
    def ram_model_2(self):
        self.ram_total_points = self.ram_total_points + 4
        print("RAM Model: DDR 4")

    print(ram_total_points);

    def result(self):
        return self.ram_total_points;
