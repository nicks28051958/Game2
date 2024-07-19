from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")


class Bow(Weapon):
    def attack(self):
        print("Боец стреляет из лука.")


class Axe(Weapon):
    def attack(self):
        print("Боец наносит удар топором.")


class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            self.weapon.attack()
        else:
            print("У бойца нет оружия!")


class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"Монстр {self.name} побежден!")
            return True
        else:
            print(f"Монстр {self.name} получил {damage} урона. Осталось здоровья: {self.health}")
            return False


def choose_weapon():
    weapons = {
        "1": Sword(),
        "2": Bow(),
        "3": Axe()
    }
    print("Выберите оружие:")
    print("1: Меч")
    print("2: Лук")
    print("3: Топор")
    choice = input("Введите номер оружия: ")
    return weapons.get(choice, Sword())  # По умолчанию выбираем меч


# Демонстрация боя
if __name__ == "__main__":
    fighter = Fighter("Рыцарь")
    monster = Monster("Гоблин", 35)

    while monster.health > 0:
        # Боец выбирает оружие перед каждым ударом
        weapon = choose_weapon()
        fighter.changeWeapon(weapon)

        # Боец атакует
        fighter.attack()
        is_defeated = monster.take_damage(10)

        if is_defeated:
            break

