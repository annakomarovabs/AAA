from pizza import Menu, ColorizeMixin, Pizza
from random import randint
import click


@click.command()
@click.option('--delivery', default=True, is_flag=True, required=False)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    print(f'👩🏼‍🍳 Приготовили за {randint(1,15)}с!')
    if delivery:
        print(f'🛵 Доставили за {randint(2,10)}с!')


@click.command()
def menu():
    """Выводит меню"""
    for dish in Menu().get_menu_for_today():
        print(f'- {Pizza(dish).dict()}')


if __name__ == '__main__':
    menu()
    order('pepperoni')
