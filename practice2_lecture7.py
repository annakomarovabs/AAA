import random
from abc import ABC, abstractmethod


class AnimeMon(ABC):
    @classmethod
    @abstractmethod
    def inc_exp(self, value):
        return

    @property
    @abstractmethod
    def exp(self):
        pass


class Pokemon(ABC):
    def __init__(self, name: str, poketype: str, exp: int = 0):
        self.name = name
        self.poketype = poketype
        self._exp = exp

    def __repr__(self):
        return f'self._exp'

    def exp(self):
        return self._exp

    def inc_exp(self, step):
        self._exp = self.exp() + step


class Digimon(ABC):
    def __init__(self, name: str, exp: int = 0):
        self.name = name
        self._exp = exp

    def __repr__(self):
        return f'self._exp'

    def exp(self):
        return self._exp

    def inc_exp(self, value: int):
        self._exp = self.exp() + value * 8


def train(pokemon: Pokemon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - pokemon.exp() % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            pokemon.inc_exp(step_size)


if __name__ == '__main__':
    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    train(bulbasaur)
    print(bulbasaur.exp())

    agumon = Digimon(name='Agumon')
    train(agumon)
    print(agumon.exp())
