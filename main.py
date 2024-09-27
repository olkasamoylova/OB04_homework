# Шаг 1: Создайте абстрактный класс для оружия
# Создайте абстрактный класс Weapon, который будет содержать абстрактный метод attack().

from abc import ABC, abstractmethod
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass
    @abstractmethod
    def get_name(self):
        pass

# Шаг 2: Реализуйте конкретные типы оружия
# Создайте несколько классов, унаследованных от Weapon, например, Sword и Bow.
# Каждый из этих классов реализует метод attack() своим уникальным способом.

class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом!"
    def get_name(self):
        return "меч"

class Bow(Weapon):
    def attack(self):
        return "наносит удар из лука!"
    def get_name(self):
        return "лук"

# Шаг 3: Модифицируйте класс Fighter
# Добавьте в класс Fighter поле, которое будет хранить объект класса Weapon.
# Добавьте метод change_weapon(), который позволяет изменить оружие бойца.

# Исходные данные:
# Есть класс Fighter, представляющий бойца.
# Есть класс Monster, представляющий монстра.
# Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.

# Шаг 4: Реализация боя
# Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.

class Fighter():
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {self.weapon.get_name()}.")

    def attack_monster(self, monster):
        if self.weapon:
           print(f"{self.name} {self.weapon.attack()}")
           monster.take_damage()
        else:
           print(f"{self.name} не может атаковать, так как у него нет оружия.")

class Monster:
    def __init__(self, name="Монстр"):
        self.name = name
        self.alive = True

    def take_damage(self):
        if self.alive:
            print(f"{self.name} побежден!")
            self.alive = False
        else:
            print(f"{self.name} уже мертв.")

fighter = Fighter("Боец")
monster = Monster()
fighter.attack_monster(monster)

sword = Sword()
fighter.change_weapon(sword)
fighter.attack_monster(monster)

# Боец выбирает лук и атакует еще раз
bow = Bow()
monster = Monster()  # Новый монстр для новой битвы
fighter.change_weapon(bow)
fighter.attack_monster(monster)
fighter.attack_monster(monster)