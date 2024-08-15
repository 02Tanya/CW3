import json
from datetime import datetime
from config import operations_path


def load_operations():
    '''Загружает данные из файла .json'''
    with open(operations_path, 'rt') as file:
        file = json.load(file)

        return file


def show_date(date):
    '''Преобразует формат представления даты в необходимый'''
    date_object = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    date_str = datetime.strftime(date_object, '%d-%m-%Y')
    return date_str


def get_card_number(moved_from):
    '''Определяет формат вывода номера карты'''
    if moved_from is not None:
        account = moved_from.split()
        account_alpha = account[:-1]
        account_alpha = ' '.join(account_alpha)
        account_digit = account[-1]
        account = (account_alpha + ' ' + account_digit[0:4] + ' ' +
                account_digit[4:6] + '**' + ' ' + '****' + ' ' +
                account_digit[-4:])
        return account


def get_account_number(moved_to):
    '''Определяет формат вывода номера счета'''
    account = moved_to.split()
    account_alpha = account[:-1]
    account_digit = account[-1]
    account_alpha = ' '.join(account_alpha)
    account = account_alpha + ' ' + '**' + account_digit[-4:]
    return account


def get_sort_transaction(operation_path):
    '''Формирует и сортирует список под заданные условия'''
    all_data = load_operations()

    list_transaction = []
    for el in all_data:
        if bool(el) and el['state'] == 'EXECUTED':
            list_transaction.append(el)

    list_transaction.sort(key=lambda transaction: transaction['date'], reverse=True)

    return list_transaction
