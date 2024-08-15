import json
from datetime import datetime
from config import operations_path


def load_operations():
    '''Загружает данные из файла .json'''
    with open(operations_path, 'rt') as file:
     #   file = f.read()
        file = json.load(file)
        return file


def date_format(date_str):
    '''Принимает дату в строковом формате и возвращает дату
    '''
    date_object = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
    return date_object


def date_show(date_str):
    '''Описание'''
    date_object = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
    date_showed = datetime.strptime(date_object, '%d-%m-%Y')
    return date_showed


# def is_executed():
#     '''Проверяет у операции наличие признака EXECUTED
#     '''
#     if data['state'] = 'EXECUTED'
#         return


def format_from_account(write_off):
    if write_off is not None:
        account = write_off.split()
        account_alpha = account[:-1]
        account_alpha = ' '.join(account_alpha)
        account_digit = account[-1]
        account = (account_alpha + ' ' + account_digit[0:4] + ' ' +
               account_digit[4:6] + '**' + ' ' + '****' + ' ' +
               account_digit[-4:])
        return account


def format_to_account(write_to):

    account = write_to.split()
    account_alpha = account[:-1]
    account_digit = account[-1]
    account_alpha = ' '.join(account_alpha)
    account = account_alpha + ' ' + '**' + account_digit[-4:]
    return account


def get_sort_transaction(json_path):
    all_information = load_operations()

    list_transaction = []
    for el in all_information:
        if bool(el) and el['state'] == 'EXECUTED':
            list_transaction.append(el)

    list_transaction.sort(
        key = lambda transaction: date_format(transaction['date']),
        reverse=True)
    return list_transaction
