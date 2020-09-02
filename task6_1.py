from time import sleep


class TrafficLight:
    __color = ["Красный", "Желтый", "Зеленый", "Желтый"]

    def running(self):
        while True:
            i = 0
            while i < 4:
                if i == 0:
                    red(f"Горит {TrafficLight.__color[i]} свет \n")
                    sleep(7)
                elif i == 1:
                    yellow(f"Горит {TrafficLight.__color[i]} свет \n")
                    sleep(2)
                elif i == 2:
                    green(f"Горит {TrafficLight.__color[i]} свет \n")
                    sleep(7)
                elif i == 3:
                    yellow(f"Горит {TrafficLight.__color[i]} свет \n")
                    sleep(2)
                i += 1


def red(text):
    print("\033[31m {}".format(text))


def yellow(text):
    print("\033[33m {}".format(text))


def green(text):
    print("\033[32m {}".format(text))


TrafficLight = TrafficLight()
TrafficLight.running()
