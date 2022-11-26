import requests
import json

from datetime import datetime
from calendar import monthrange


def get_url(v_code, yyyy, mm, dd):
    return f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={v_code}&date={yyyy}{mm}{dd}&json'


def val_code():
    val_code_list = ['USD', 'EUR', 'GBP', 'CHF']
    while True:
        result = input(f'Вкажіть код валюти за наведених без лапок {val_code_list}: ')
        if result.upper() in val_code_list:
            break
        else:
            print('Ви ввели не вірне значення. Спробуйте ще раз.')
    return result


def check_input(obj_val, obj_name, current_y_m_d):
    obj_val_len = 4 if obj_name == 'val_year' else 2
    try:
        int(obj_val)
    except ValueError:
        print('Ви ввели не вірне значення. Спробуйте ще раз.')
        return False
    if len(obj_val) == obj_val_len and int(obj_val) <= current_y_m_d:
        return obj_val
    else:
        return False


def val_year():
    while True:
        result = check_input(input('Вкажіть рік запиту у форматі "yyyy": '), val_year.__name__, datetime.now().year)
        if result is not False:
            return result


def val_month(yyyy):
    if int(yyyy) == datetime.now().year:
        month_mm = datetime.now().month
    else:
        month_mm = 12
    while True:
        result = check_input(input('Вкажіть місяць запиту у форматі "mm": '), val_month.__name__, month_mm)
        if result is not False:
            return result


def val_day(yyyy, mm):
    yyyy = int(yyyy)
    mm = int(mm)
    if yyyy == datetime.now().year and mm == datetime.now().month:
        day_dd = datetime.now().day
    else:
        day_dd = monthrange(yyyy, mm)[1]
    while True:
        result = check_input(input('Вкажіть день запиту у форматі "dd": '), val_day.__name__, day_dd)
        if result is not False:
            return result


def current_money():
    while True:
        try:
            result = float(input('Введіть суму у UAH для обміну: '))
            return result
        except ValueError:
            print('Ви ввели не вірне значення. Спробуйте ще раз.')


while True:
    val_code_cc = val_code()
    val_year_yyyy = val_year()
    val_month_mm = val_month(val_year_yyyy)
    val_day_dd = val_day(val_year_yyyy, val_month_mm)
    current_money_ex = current_money()
    url = get_url(val_code_cc, val_year_yyyy, val_month_mm, val_day_dd)
    response = requests.get(url)
    if response.status_code == 200:
        try:
            content = json.loads(response.content)[0]
        except IndexError:
            print(f'\n\tДаних за {val_year_yyyy} не існує. Спробуйте ще раз.\n')
            continue
        if content.get('message'):
            print(f'\n\tmsg: {content["message"]}\n')
            continue
        recalculated_value = round(float(current_money_ex) / content["rate"], 2)
        print(f'\n\tСтаном на {content["exchangedate"]} за курсом обміну "{content["txt"]}" ({content["cc"]}): '
              f'{content["rate"]} \nпри обміні {current_money_ex} UAH Ви отримаєте: {recalculated_value} '
              f'{content["cc"]}')
        break
    else:
        print(f'Ви зробили не вірний запит. Статус запиту: {response.status_code}')
