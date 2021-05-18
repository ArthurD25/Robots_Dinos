from weapon import Weapon
from robot import Robot
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
from battlefield import Battlefield

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_weapon = Weapon('sword', 100)
    my_weapon2 = Weapon('hammer', 200)
    my_weapon3 = Weapon('Dagger', 70)
  #  print(my_weapon.type)
    #print(my_weapon.attack_power)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
    Robot_1 = Robot('Josh', 9000, 100, my_weapon2)
    print(Robot_1.name)
    print(Robot_1.power_level)
    print(Robot_1.health)
    print(my_weapon2.type)

    Robot_2 = Robot('Tom', 9000, 100, my_weapon)
    print(Robot_2.name)
    print(Robot_2.power_level)
    print(Robot_2.health)
    print(my_weapon.type)

    Robot_3 = Robot('Jeff', 9000, 100, my_weapon3)
    print(Robot_3.name)
    print(Robot_3.power_level)
    print(Robot_3.health)
    print(my_weapon3.type)

    Dinosaur_1 = Dinosaur('Winged', 10, 10, 100 )
    print(Dinosaur_1.type)
    print(Dinosaur_1.energy)
    print(Dinosaur_1.health)
    print(Dinosaur_1.attack_power)

    Dinosaur_2 = Dinosaur('T-Rex', 10, 10, 100)
    print(Dinosaur_2.type)
    print(Dinosaur_2.energy)
    print(Dinosaur_2.health)
    print(Dinosaur_2.attack_power)

    Dinosaur_3 = Dinosaur('Dragon', 10, 10, 100)
    print(Dinosaur_3.type)
    print(Dinosaur_3.energy)
    print(Dinosaur_3.health)
    print(Dinosaur_3.attack_power)

    Robot_1.attack(Dinosaur)
    Dinosaur_1.attack(Robot)