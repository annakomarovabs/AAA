from random import randint
from typing import Callable


class Menu:
    size = {'XL', 'L'}
    receipts = {'pepperoni': ['tomato sauce', 'mozzarella', 'pepperoni'],
                'margherita': ['tomato sauce', 'mozzarella', 'tomatoes'],
                'hawaiian': ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']}

    def get_menu_for_today(self):
        return list(self.receipts.keys())


class EmojiMixin:
    """adding emoji to receipts"""
    emoji = {
        'pepperoni': '🍕',
        'margherita': '🧀',
        'hawaiian': '🍍'
    }

    def dict(self):
        return {f'{self.type} {self.emoji[self.type]}': self.receipts[self.type]}


class Pizza(EmojiMixin, Menu):
    def __init__(self, type: str):
        if type not in self.get_menu_for_today():
            raise ValueError("not in menu today:(")
        else:
            self.type = type

    def __eq__(self, other):
        return self.type == other.type


def log(func: Callable) -> Callable:
    def wrapper(pizza):
        print(f'{func.__name__} - {randint(1,5)}c!')

    return wrapper


def log2(message: str) -> Callable:
    def decorator(func):
        def wrapper(pizza):
            print(message.format(randint(1, 5)))
        return wrapper
    return decorator


@log
def bake(pizza):
    """Готовит пиццу"""
    pass


@log2('🛵 Доставили за {}с!')
def delivery(pizza):
    """Доставляет пиццу"""
    pass


@log2('🏠 Забрали за {}с!')
def pickup(pizza):
    """Самовывоз"""
    pass


if __name__ == '__main__':
    bake(Pizza('margherita'))
    pickup(Pizza('margherita'))
    delivery(Pizza('margherita'))
