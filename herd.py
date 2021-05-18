from dinosaur import Dinosaur
class Herd:
    def __init__(self):
        self.herd_of_robots = []

    def create_herd(self):
        Dinosaur_1 = Dinosaur()
        Dinosaur_2 = Dinosaur()
        Dinosaur_3 = Dinosaur()
        self.herd_of_robots.append(Dinosaur_1)
        self.herd_of_robots.append(Dinosaur_2)
        self.herd_of_robots.append(Dinosaur_3)
