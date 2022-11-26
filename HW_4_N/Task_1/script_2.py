import json
import exceptions


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


def decorator(func):
    def wrapper(user_id: str, company_id: str):
        get_user = get_obj('users_db.json', user_id, f'"Користувач id={user_id}:"')
        result = func(company_id)
        if int(company_id) not in get_user['companies']:
            raise exceptions.NoAccess(f'"Користувач id={user_id}"')
        return result
    return wrapper


@decorator
def get_company_city(company_id: str):
    get_company = get_obj('company_db.json', company_id, f'"Компанія id={company_id}:"')
    company_city_ = get_company['city']
    return company_city_


company_id_ = input('Введіть id компанії: ')
user_id_ = input('Введіть id користувача: ')
company_city = get_company_city(user_id_, company_id_)
if company_city:
    print(f"Компанія id={company_id_} зареєстрована у місті: {company_city}")
print('Завершення програми')
