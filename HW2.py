{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [],
   "source": [
    "data_path = '/Users/anna-komarovabs/Desktop/ААА/python/Corp Summary.csv'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "def step1():\n",
    "    \"\"\"\n",
    "    Параметры:\n",
    "    - alpha: уровень значимости\n",
    "    - beta: инвертированная мощность критерия. мощность = 1 - beta.\n",
    "    - p: истинная вероятность того, что пользователю понравится дизайн.\n",
    "    Возвращает:\n",
    "    - number_of_users: int\n",
    "        - количество людей, которым надо показать дизайн.\n",
    "    \"\"\"\n",
    "    print(\n",
    "        'Выберите действие: \\n' \n",
    "        '1 - выведите иерархию' \n",
    "        '2 - выведите сводный отчет'\n",
    "        '3 - сохраните сводный отчет'\n",
    "    )\n",
    "    option = ''\n",
    "    options = {'1': 1, '2': 2, \"3\": 3}\n",
    "    while option not in options:\n",
    "        print('Выберите: {}/{}/{}'.format(*options))\n",
    "        option = input()\n",
    "\n",
    "    if options[option]==1:\n",
    "        return hierarchy(file_path = data_path)\n",
    "    elif options[option]==2:\n",
    "        return report(data_path)\n",
    "    return save_report(data_path)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Выберите действие: \n",
      "1 - выведите иерархию2 - выведите сводный отчет3 - сохраните сводный отчет\n",
      "Выберите: 1/2/3\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 3\n"
     ]
    }
   ],
   "source": [
    "step1()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "def hierarchy(file_path: \"str\"):\n",
    "    \"\"\"\n",
    "    Параметры:\n",
    "    - file_path: путь к файлу с данными\n",
    "    Возвращает:\n",
    "    -словарь: {департамент}:[отделы]\n",
    "    \"\"\"\n",
    "    with open(file_path, newline='\\n', encoding='utf-8') as f:\n",
    "        reader = csv.reader(f)\n",
    "        dict = {}\n",
    "        teams = []\n",
    "        for row in reader:\n",
    "            row = row[0].split(\";\")\n",
    "            if row[1] not in dict:\n",
    "                dict[row[1]] = [row[2]]\n",
    "            else:\n",
    "                dict[row[1]].append(row[2])\n",
    "        for key in dict:\n",
    "            teams = list(set(dict[key]))\n",
    "            teams_to_str = ', '.join([str(elem) for elem in teams])\n",
    "            print(f'{key}:', teams_to_str)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "def report(file_path: \"str\"):\n",
    "    \"\"\"\n",
    "    Параметры:\n",
    "    - file_path: путь к файлу с данными\n",
    "    Возвращает:\n",
    "    -словарь: {отдел}:[зарплатная вилка, количество сотрудников]\n",
    "    \"\"\"\n",
    "    \n",
    "    with open(data_path, newline='\\n', encoding='utf-8') as f:\n",
    "        reader = csv.reader(f)\n",
    "        dict = {}\n",
    "        wages = []\n",
    "        for row in reader:\n",
    "            row = row[0].split(\";\")\n",
    "            if row[1] != \"Департамент\" and row[1] not in dict:\n",
    "                    dict[row[1]] = [row[5]]\n",
    "            elif row[1] != \"Департамент\":\n",
    "                    dict[row[1]].append(row[5])\n",
    "        for key in dict:\n",
    "            wages = list(set(dict[key]))\n",
    "            wages = [int(x) for x in wages]\n",
    "            min_wage, max_wage = min(wages), max(wages)\n",
    "            mean_wage = int(sum(wages)/len(wages)) \n",
    "            print(f'Департамент {key}:', \"1)зарплатная вилка:\", min_wage, \" - \", max_wage, \"; \", \"2) средняя зарплата в департаменте:\", \n",
    "                 mean_wage, \"; \", \"3) количество сотрудников:\", len(wages))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [],
   "source": [
    "def save_report(file_path: \"str\"):\n",
    "     \"\"\"\n",
    "    Параметры:\n",
    "    - file_path: путь к файлу с данными\n",
    "    Возвращает:\n",
    "    -.csv file\n",
    "    \"\"\"\n",
    "        \n",
    "    with open('./Corp Report.csv', 'w') as f:\n",
    "        REPORT_HEADER_FIELDS = (\n",
    "            'Департамент',\n",
    "            'Отделы',\n",
    "            'Минимальная зарплата',\n",
    "            'Максимальная зарплата',\n",
    "            'Средняя зарплата',\n",
    "            'Количество сотрудников',\n",
    "        )\n",
    "        out_file = csv.writer(f, delimiter=';')\n",
    "        out_file.writerow(REPORT_HEADER_FIELDS)\n",
    "        dict1, dict2, dict0 = {}, {}, {}\n",
    "        with open(data_path, newline='\\n', encoding='utf-8') as f:\n",
    "            reader = csv.reader(f)\n",
    "            for row in reader:\n",
    "                row = row[0].split(\";\")\n",
    "                if row[1] != \"Департамент\" and row[1] not in dict1:\n",
    "                        dict1[row[1]] = [row[5]]\n",
    "                elif row[1] != \"Департамент\":\n",
    "                        dict1[row[1]].append(row[5])\n",
    "                if row[1] != \"Департамент\" and row[1] not in dict2:\n",
    "                        dict2[row[1]] = [row[2]]\n",
    "                elif row[1] != \"Департамент\":\n",
    "                        dict2[row[1]].append(row[2])\n",
    "        for key in dict2:\n",
    "            teams = list(set(dict2[key]))\n",
    "            teams_to_str = ', '.join([str(elem) for elem in teams])\n",
    "            dict0[key] = [teams_to_str]\n",
    "        for key in dict1:\n",
    "            wages = list(set(dict1[key]))\n",
    "            wages = [int(x) for x in wages]\n",
    "            min_wage, max_wage = min(wages), max(wages)\n",
    "            mean_wage = int(sum(wages)/len(wages)) \n",
    "            dict0[key].append(min_wage)\n",
    "            dict0[key].append(max_wage)\n",
    "            dict0[key].append(mean_wage)\n",
    "            dict0[key].append(len(wages))\n",
    "        for key in dict0:\n",
    "            out_file.writerow((\n",
    "                key,\n",
    "                dict0[key][0], \n",
    "                dict0[key][1],\n",
    "                dict0[key][2],\n",
    "                dict0[key][3],\n",
    "                dict0[key][4]\n",
    "            ))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
