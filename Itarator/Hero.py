from MonsterBook import Monster, BigBookOfBeasts

class Hero:
    def __init__(self):
        self._big_book_of_beasts = BigBookOfBeasts()
        self._big_book_of_beasts.add_monster(Monster("ドラキー", 10))
        self._big_book_of_beasts.add_monster(Monster("ほのおのせんし", 150))
        self._big_book_of_beasts.add_monster(Monster("スライムナイト", 80))

    def use_big_book_of_beasts(self):
        ite = self._big_book_of_beasts.iterator()
        while ite.has_next():
            monster = ite.next()
            print(monster)