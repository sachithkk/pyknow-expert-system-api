from pyknow import *
import logging as logger

from app import flaskAppInstance


class CPU(Fact):
    pass;


class CPUService(KnowledgeEngine):

    cpu_total_points = 0

    @DefFacts()
    def __const__(self):
        logger.info("Called Defacts method.")
        # time.sleep(10)
        # self.connect_open()
        yield Fact(cpu_init=True)

    #
    # CPU type point calculation.
    #
    @Rule(CPU(cpu_model="core i3"))
    def cpu_model_1(self):
        self.cpu_total_points = self.cpu_total_points + 3
        print("Cpu Model: core i3")

    @Rule(CPU(cpu_model="core i5"))
    def cpu_model_2(self):
        self.cpu_total_points = self.cpu_total_points + 5
        print("Cpu Model: core i5")

    @Rule(CPU(cpu_model="core i7"))
    def cpu_model_3(self):
        self.cpu_total_points = self.cpu_total_points + 7
        print("Cpu Model: core i7")

    @Rule(CPU(cpu_model="core i9"))
    def cpu_model_4(self):
        self.cpu_total_points = self.cpu_total_points + 9
        print("Cpu Model: core i9")

    #
    # CPU generation point calculation.
    #
    @Rule(CPU(cpu_genaration="generation 1"))
    def cpu_generation_1(self):
        self.cpu_total_points = self.cpu_total_points + 1
        print("Cpu Generation: 1")

    @Rule(CPU(cpu_genaration="generation 2"))
    def cpu_generation_2(self):
        self.cpu_total_points = self.cpu_total_points + 2
        print("Cpu Generation: 2")

    @Rule(CPU(cpu_genaration="generation 3"))
    def cpu_generation_3(self):
        self.cpu_total_points = self.cpu_total_points + 3
        print("Cpu Generation: 3")

    @Rule(CPU(cpu_genaration="generation 4"))
    def cpu_generation_4(self):
        self.cpu_total_points = self.cpu_total_points + 4
        print("Cpu Generation: 4")

    @Rule(CPU(cpu_genaration="generation 5"))
    def cpu_generation_5(self):
        self.cpu_total_points = self.cpu_total_points + 5
        print("Cpu Generation: 5")

    @Rule(CPU(cpu_genaration="generation 6"))
    def cpu_generation_6(self):
        self.cpu_total_points = self.cpu_total_points + 6
        print("Cpu Generation: 6")

    @Rule(CPU(cpu_genaration="generation 7"))
    def cpu_generation_7(self):
        self.cpu_total_points = self.cpu_total_points + 7
        print("Cpu Generation: 7")

    @Rule(CPU(cpu_genaration="generation 8"))
    def cpu_generation_8(self):
        self.cpu_total_points = self.cpu_total_points + 8
        print("Cpu Generation: 8")

    @Rule(CPU(cpu_genaration="generation 9"))
    def cpu_generation_9(self):
        self.cpu_total_points = self.cpu_total_points + 9
        print("Cpu Generation: 9")

    #
    # CPU speed point calculation.
    #
    @Rule(CPU(cpu_speed= 1))
    def cpu_speed_1(self):
        self.cpu_total_points = self.cpu_total_points + 1
        print("Cpu Speed: 1 Ghz")

    @Rule(CPU(cpu_speed= 2))
    def cpu_speed_2(self):
        self.cpu_total_points = self.cpu_total_points + 2
        print("Cpu Speed: 2 Ghz")

    @Rule(CPU(cpu_speed= 3))
    def cpu_speed_3(self):
        self.cpu_total_points = self.cpu_total_points + 3
        print("Cpu Speed: 3 Ghz")

    @Rule(CPU(cpu_speed= 4))
    def cpu_speed_4(self):
        self.cpu_total_points = self.cpu_total_points + 4
        print("Cpu Speed: 4 Ghz")

    @Rule(CPU(cpu_speed= 5))
    def cpu_speed_5(self):
        self.cpu_total_points = self.cpu_total_points + 5
        print("Cpu Speed: 5 Ghz")



    print(cpu_total_points);

    def result(self):
        return self.cpu_total_points;
