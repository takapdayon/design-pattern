from Aggregate import Aggregate
from Iterator import Iterator

# モンスター図鑑でのみ使うのでいろいろ端折ります
class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def __str__(self):
        return f"Name: {self.name} HP: {self.hp}"

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp


class BigBookOfBeasts(Aggregate):

    def __init__(self):
        self.monsters: List[Monster] = []

    def add_monster(self, monster: Monster):
        self.monsters.append(monster)

    def get_monster(self, index):
        return self.monsters[index]

    def get_monster_count(self):
        return len(self.monsters)

    def iterator(self):
        return BigBookOfBeastsIterator(self)


class BigBookOfBeastsIterator(Iterator):
    def __init__(self, big_book_of_beasts: BigBookOfBeasts):
        self.big_book_of_beasts = big_book_of_beasts
        self._index = 0

    def has_next(self) -> bool:
        return bool(self.big_book_of_beasts.get_monster_count() > self._index)

    def next(self) -> object:
        monster = self.big_book_of_beasts.get_monster(self._index)
        self._index += 1
        return monster