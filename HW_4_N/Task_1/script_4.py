import json
import exceptions
import logging
import time

from datetime import datetime as dt


def get_content_from_db(db_file: str):
    with open(db_file, encoding='utf-8') as content_db:
        result = json.load(content_db)
    return result


def get_obj(file_db: str, obj_id: str, exception_msg: str):
    obj_db = get_content_from_db(file_db)
    obj = obj_db.get(obj_id)
    if obj is None:
        raise exceptions.NotFound(exception_msg)
    return obj


def run_time_counter(func):
    def wrapper(*args):
        start_func = dt.now().strftime('%H:%M:%S')
        st = time.time()
        result = func(*args)
        et = time.time()
        logging.debug(f'Функція запущена: {start_func}. Час виконання функції: {(et - st)} s')
        return result
    return wrapper


def exception_handler(func):
    def wrapper(*args):
        try:
            return func(*args)
        except Exception as e_msg:
            logging.warning(e_msg, exc_info=True)
    return wrapper


def user_access_company(func):
    def wrapper(user_id: str, company_id: str):
        get_user = get_obj('users_db.json', user_id, f'"Користувач id={user_id}"')
        result = func(company_id)
        if int(company_id) not in get_user['companies']:
            raise exceptions.NoAccess(f'"Користувач id={user_id}"')
        return result
    return wrapper


@run_time_counter
@exception_handler
@user_access_company
def get_company_city(company_id: str):
    get_company = get_obj('company_db.json', company_id, f'"Компанія id={company_id}"')
    company_city_ = get_company['city']
    return company_city_


# block settings
format_template = '%(asctime)s [%(levelname)s]: %(message)s'
logging_into_file = True

if logging_into_file:
    logging.basicConfig(level=logging.DEBUG, format=format_template, filename='HW4_log.txt', encoding='utf-8')
else:
    logging.basicConfig(level=logging.DEBUG, format=format_template, encoding='utf-8')
# end_block settings

company_id_ = input('Введіть id компанії: ')
user_id_ = input('Введіть id користувача: ')
company_city = get_company_city(user_id_, company_id_)
if company_city:
    print(f"Компанія id={company_id_} зареєстрована у місті: {company_city}")
print('Завершення програми')
