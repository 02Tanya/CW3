from datetime import datetime

date = "2019-08-26T10:50:58.294041"

# def date_format():
#     '''Принимает дату в строковом формате и возвращает дату
#     '''
#     date_object = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
#     return date_object


def date_show():
    ''''''
    date_object = str(datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f'))
    # date_str = datetime.strptime(date_object, '%d-%m-%Y')
    # return date_str
    return date_object

# print(date_format())
print(date_show())