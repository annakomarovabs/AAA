def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        "Взяла зонтик и начала красить. а что не так с уткой?"
    )


def step2_no_umbrella():
    print(
        "Выпила коктейль и пошла домой. Так и не взяв зонтик, она встретила такси, которое отвезло ее в вытрезвитель."
    )


if __name__ == '__main__':
    step1()
