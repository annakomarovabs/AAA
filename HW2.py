#!/usr/bin/env python
# coding: utf-8

# In[95]:


import csv
from collections import defaultdict


# In[96]:


data_path = '/Users/anna-komarovabs/Desktop/ААА/python/Corp Summary.csv'


# In[97]:


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
    options = {'1': 1, '2': 2, "3": 3}
    while option not in options:
        print('Выберите: {}/{}/{}'.format(*options))
        option = input()

    if options[option]==1:
        out = print_hierarchy(file_path = data_path)
        for key in out:
            print(f'{key}: {out[key]}')
    elif options[option]==2:
        out = print_report(file_path = data_path)
        for key in out:
            print(f'Департамент {key}: 1)зарплатная вилка: {out[key][0]} - {out[key][1]}; 2) средняя зарплата в департаменте: {out[key][2]}; '
                  f'3) количество сотрудников: {out[key][3]}')
    else:
        return save_report(data_path)


# In[98]:


def print_hierarchy(file_path: "str"):
    """
    Параметры:
    - file_path: путь к файлу с данными
    Возвращает:
    -словарь: {департамент:{отделы}}
    """
    
    with open(file_path, newline='\n', encoding='utf-8') as data:
        reader = csv.reader(data, delimiter = ";")
        hierarchy = defaultdict(list)
        header = next(reader)
        for row in reader:
            hierarchy[row[1]] += [row[2]]
        for department in hierarchy:
            hierarchy[department] = ', '.join(str(e) for e in set(hierarchy[department]))
    return hierarchy


# In[99]:


def print_report(file_path: "str"):
    """
    Параметры:
    - file_path: путь к файлу с данными
    Возвращает:
    -словарь: {отдел:[зарплатная вилка, количество сотрудников]}
    """
    
    with open(file_path, newline='\n', encoding='utf-8') as data:
        reader = csv.reader(data, delimiter = ";")
        wages_by_dep = defaultdict(list)
        report = defaultdict(list)
        header = next(reader)
        for row in reader:
            wages_by_dep[row[1]] += [row[5]]
        for department in wages_by_dep:
            wages = [int(x) for x in wages_by_dep[department]]
            report[department] += min(wages), max(wages), int(sum(wages)/len(wages)), len(wages)
    return report


# In[100]:


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
        hierarchy = print_hierarchy(file_path)
        report = print_report(file_path)
        full_information = {key:[hierarchy[key], report[key]] for key in hierarchy}
        for department in full_information:
            out_file.writerow((
                department, 
                full_information[department][0], 
                full_information[department][1][0],
                full_information[department][1][1],
                full_information[department][1][2],
                full_information[department][1][3]
            ))


# In[104]:


menu()


# In[ ]:




