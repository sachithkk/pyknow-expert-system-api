from pyknow import *
import logging as logger

class Laptop(Fact):
    pass;

class  LaptopService(KnowledgeEngine):


    # def __init__(self, a):
    #     self.a = a
    #     print("This is model name : "+ self.a)


    compational_power_point = 0

    @DefFacts()
    def __const__(self):
        logger.info("Called Defacts method.")
        yield Fact(laptop_init=True)

    #
    # CPU type point calculation.
    #
    @Rule(Laptop(cpuModel="core i3"))
    def cpu_model_1(self):
        self.compational_power_point = self.compational_power_point + 3
        print(self.compational_power_point)

    @Rule(Laptop(cpuModel="core i5"))
    def cpu_model_2(self):
        self.compational_power_point = self.compational_power_point + 5
        print(self.compational_power_point)

    @Rule(Laptop(cpuModel="core i7"))
    def cpu_model_3(self):
        self.compational_power_point = self.compational_power_point + 7
        print(self.compational_power_point)

    @Rule(Laptop(cpuModel="core i9"))
    def cpu_model_4(self):
        self.compational_power_point = self.compational_power_point + 10
        print(self.compational_power_point)


    #
    # CPU core point calculation.
    #

    @Rule(Laptop(cpuCoresSize="2"))
    def cpu_core_1(self):
        self.compational_power_point = self.compational_power_point + 1

    @Rule(Laptop(cpuCoresSize="4"))
    def cpu_core_2(self):
        self.compational_power_point = self.compational_power_point + 2
        print(self.compational_power_point)

    @Rule(Laptop(cpuCoresSize="6"))
    def cpu_core_3(self):
        self.compational_power_point = self.compational_power_point + 3

    @Rule(Laptop(cpuCoresSize="8"))
    def cpu_core_4(self):
        self.compational_power_point = self.compational_power_point + 6

    @Rule(Laptop(cpuCoresSize="10"))
    def cpu_core_5(self):
        self.compational_power_point = self.compational_power_point + 8

    @Rule(Laptop(cpuCoresSize="12"))
    def cpu_core_6(self):
        self.compational_power_point = self.compational_power_point + 10

    #
    # CPU cache point calculation.
    #

    @Rule(Laptop(cpuCachSize="3"))
    def cpu_cache_1(self):
        self.compational_power_point = self.compational_power_point + 1

    @Rule(Laptop(cpuCachSize="4"))
    def cpu_cache_2(self):
        self.compational_power_point = self.compational_power_point + 2

    @Rule(Laptop(cpuCachSize="6"))
    def cpu_cache_3(self):
        self.compational_power_point = self.compational_power_point + 3
        print(self.compational_power_point)

    @Rule(Laptop(cpuCachSize="8"))
    def cpu_cache_4(self):
        self.compational_power_point = self.compational_power_point + 4

    @Rule(Laptop(cpuCachSize="9"))
    def cpu_cache_5(self):
        self.compational_power_point = self.compational_power_point + 5

    #
    # RAM type point calculation.
    #

    @Rule(Laptop(ramType="DDR3"))
    def ram_type_1(self):
        self.compational_power_point = self.compational_power_point + 1

    @Rule(Laptop(ramType="DDR4"))
    def ram_type_2(self):
        self.compational_power_point = self.compational_power_point + 3

    #
    # RAM size point calculation.
    #

    @Rule(Laptop(ramSize="2"))
    def ram_size_1(self):
        self.compational_power_point = self.compational_power_point + 2

    @Rule(Laptop(ramSize="4"))
    def ram_size_1(self):
        self.compational_power_point = self.compational_power_point + 5

    @Rule(Laptop(ramSize="6"))
    def ram_size_1(self):
        self.compational_power_point = self.compational_power_point + 6

    @Rule(Laptop(ramSize="8"))
    def ram_size_1(self):
        self.compational_power_point = self.compational_power_point + 7

    @Rule(Laptop(ramSize="16"))
    def ram_size_1(self):
        self.compational_power_point = self.compational_power_point + 10

    #
    # STORAGE type point calculation.
    #

    @Rule(Laptop(storageType="HDD"))
    def storage_type_1(self):
        self.compational_power_point = self.compational_power_point + 1

    @Rule(Laptop(storageType="SDD"))
    def storage_type_2(self):
        self.compational_power_point = self.compational_power_point + 3

    #
    # STORAGE size point calculation.
    #

    @Rule(Laptop(storageSize="128 GB"))
    def storage_size_1(self):
        self.compational_power_point = self.compational_power_point + 2

    @Rule(Laptop(storageSize="256 GB"))
    def storage_size_2(self):
        self.compational_power_point = self.compational_power_point + 3

    @Rule(Laptop(storageSize="512 GB"))
    def storage_size_3(self):
        self.compational_power_point = self.compational_power_point + 4

    @Rule(Laptop(storageSize="1000 GB"))
    def storage_size_4(self):
        self.compational_power_point = self.compational_power_point + 5

    #
    # BATTERY type point
    #

    @Rule(Laptop(batteryType="Li-Pol"))
    def battery_type_1(self):
        self.compational_power_point = self.compational_power_point + 1

    @Rule(Laptop(batteryType="Li-Ion"))
    def battery_type_1(self):
        self.compational_power_point = self.compational_power_point + 3