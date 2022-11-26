import json
import exceptions


def get_content_from_db(db_file):
    with open(db_file, encoding='utf-8') as content_db:
        result = json.load(content_db)
    return result


def get_company_city(company_id):
    company_db = get_content_from_db('company_db.json')
    get_company = company_db.get(company_id)
    if get_company is None:
        raise exceptions.NotFound(f'Компанія id={company_id}:')
    else:
        company_city_ = get_company['city']
    return company_city_


company_id_ = input('Введіть id компанії: ')
company_city = get_company_city(company_id_)
if company_city:
    print(f"Компанія id={company_id_} зареєстрована у місті: {company_city}")
print('Завершення програми')
