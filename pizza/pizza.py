from random import randint
from typing import Callable


class Menu:
    sizes = {'XL', 'L'}
    receipts = {'pepperoni': ['tomato sauce', 'mozzarella', 'pepperoni'],
                'margherita': ['tomato sauce', 'mozzarella', 'tomatoes'],
                'hawaiian': ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']}

    def get_menu_for_today(self):
        return list(self.receipts.keys())

    def get_possible_sizes(self):
        return self.sizes


class EmojiMixin:
    """adding emoji to receipts"""
    emoji = {
        'pepperoni': '🍕',
        'margherita': '🧀',
        'hawaiian': '🍍'
    }

    def dict(self):
        return {f'{self.type_} {self.emoji[self.type_]}': self.receipts[self.type_]}


class Pizza(EmojiMixin, Menu):
    def __init__(self, type_: str, size: str):
        if type_ not in self.get_menu_for_today() or size not in self.sizes:
            raise ValueError("not in menu today:(")
        else:
            self.type_ = type_
            self.size = size

    def __eq__(self, other):
        return self.type_ == other.type_ and self.size == other.size


def log(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} - {randint(1,5)}c!')
        result = func(*args, **kwargs)
        return result
    return wrapper


def log2(message: str) -> Callable:
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(message.format(randint(1, 5)))
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@log
def bake(pizza, size):
    """Готовит пиццу"""


@log2('🛵 Доставили за {}с!')
def delivery(pizza, size):
    """Доставляет пиццу"""


@log2('🏠 Забрали за {}с!')
def pickup(pizza, size):
    """Самовывоз"""


if __name__ == '__main__':
    print(bake('margherita', 'L'))
    pickup('margherita', 'L')
    delivery('margherita', 'L')
    want = Pizza('pepperoni', 'L')
    want2 = Pizza('margherita', 'XL')
    print(want == want2)
