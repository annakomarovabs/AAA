import csv
from collections import defaultdict

data_path = '/Users/anna-komarovabs/Desktop/ААА/python/Corp Summary.csv'


def menu():
    """
    На вход:
    - {1,2,3} - опции
    На выход:
    - вызывает функции в соответствии с опциями
    """
    print(
        'Выберите действие: \n' 
        '1 - выведите иерархию \n' 
        '2 - выведите сводный отчет \n'
        '3 - сохраните сводный отчет \n'
    )
    option = ''
    options = {'1': 1, '2': 2, '3': 3}
    while option not in options:
        print('Выберите: {}/{}/{}'.format(*options))
        option = input()

    if options[option] == 1:
        out = get_hierarchy(file_path=data_path)
        for key in out:
            print(f'{key}: {out[key]}')
    elif options[option] == 2:
        out = get_report(file_path=data_path)
        for key in out:
            print(f'Департамент {key}: 1)зарплатная вилка: {out[key][0]} - {out[key][1]}; '
                  f'2) средняя зарплата в департаменте: {out[key][2]}; '
                  f'3) количество сотрудников: {out[key][3]}')
    else:
        return save_report(data_path)


def read(file_path: "str", target: int):
    """
    Параметры:
    - file_path: путь к файлу с данными
    - target: что надо вывести: сводные данные 1 - по департаментам/ 2 - по зарплатам/ 3 - оба
    Возвращает:
    -словари: {департамент:{отделы}} и {департамент:{зарплаты}}
    """

    with open(file_path, newline='\n', encoding='utf-8') as data:
        reader = csv.DictReader(data, delimiter=";")
        hierarchy = defaultdict(list)
        wages_by_dep = defaultdict(list)
        next(reader)
        for row in reader:
            hierarchy[row["Департамент"]].append(row["Отдел"])
            wages_by_dep[row["Департамент"]].append(int(row["Оклад"]))
        if target == 1:
            return hierarchy
        elif target == 2:
            return wages_by_dep
        else:
            return hierarchy, wages_by_dep


def get_hierarchy(file_path: "str"):
    """
    Параметры:
    - file_path: путь к файлу с данными
    Возвращает:
    -словарь: {департамент: отделы}
    """

    hierarchy = read(file_path, 1)
    for dep in hierarchy:
        hierarchy[dep] = ', '.join(set(hierarchy[dep]))
    return hierarchy


def get_report(file_path: "str"):
    """
    Параметры:
    - file_path: путь к файлу с данными
    Возвращает:
    -словарь: {отдел:[зарплатная вилка, количество сотрудников]}
    """

    wages_by_dep = read(file_path, 2)
    report = defaultdict(list)
    for dep in wages_by_dep:
        wages = wages_by_dep[dep]
        report[dep] += min(wages), max(wages), int(sum(wages) / len(wages)), len(wages)
    return report


def save_report(file_path: "str"):
    """
    Параметры:
    - file_path: путь к файлу с данными
    Возвращает:
    -.csv file
    """

    with open('./Corp Report.csv', 'w') as f:
        report_header = (
            "Департамент",
            "Отделы",
            "Минимальная зарплата",
            "Средняя зарплата",
            "Количество сотрудников"
        )
        out_file = csv.writer(f, delimiter=';')
        out_file.writerow(report_header)
        hierarchy, report = get_hierarchy(file_path), get_report(file_path)
        full_information = {key: [hierarchy[key], report[key]] for key in hierarchy}
        for department in full_information:
            out_file.writerow((
                department,
                full_information[department][0],
                full_information[department][1][0],
                full_information[department][1][1],
                full_information[department][1][2],
                full_information[department][1][3]
            ))


menu()

if __name__ == '__main__':
    menu()
