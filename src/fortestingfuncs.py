from datetime import datetime

def date_format(date):
    '''Принимает дату в строковом формате и возвращает дату
    '''
    date_object = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return date_object

print(date_format("2019-04-12T17:27:27.896421"))

def date_show(date):
    '''Описание'''
    date_object = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    date_str = datetime.strftime(date_object, '%d-%m-%Y')
    return date_str

print(date_show("2019-04-12T17:27:27.896421"))