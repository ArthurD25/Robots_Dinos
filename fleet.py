from robot import Robot
class Fleet:
    def __init__(self):
        self.fleet_of_robots = []

    def create_fleet(self):
        Robot_1 = Robot()
        Robot_2 = Robot()
        Robot_3 = Robot()
        self.fleet_of_robots.append(Robot_1)
        self.fleet_of_robots.append(Robot_2)
        self.fleet_of_robots.append(Robot_3)
