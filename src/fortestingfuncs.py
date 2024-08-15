def get_accountnumber(write_off):
    '''Определяет формат вывода номера карты или счета'''
    if write_off is not None:
        account = write_off.split()
        account_alpha = account[:-1]
        account_alpha = ' '.join(account_alpha)
        account_digit = account[-1]
        account = (account_alpha + ' ' + account_digit[0:4] + ' ' +
               account_digit[4:6] + '**' + ' ' + '****' + ' ' +
               account_digit[-4:])
        return account


    s1 = col.get('from')
    s2 = col.get('to')

    def form_line(text: str):
        lst = text.split(' ')
        num = lst[-1]
        f_num = num[0:4] + ' ' + num[4:6] + '** **** ' + num[-4:]
        return ' '.join(lst[:-1]) + ' ' + f_num

    if s1 is None and s2[0:2] == 'Сч':
        return '-> ' + s2[:4] + ' ' + s2[-4:].rjust(6, '*')
    elif s1 is None:
        return '-> ' + form_line(s2)
    elif s1.startswith('Сч') and s2[:2] != 'Сч':
        agent = s1[:4] + ' ' + s1[-4:].rjust(6, '*')

def format_to_account(write_to):

    account = write_to.split()
    account_alpha = account[:-1]
    account_digit = account[-1]
    account_alpha = ' '.join(account_alpha)
    account = account_alpha + ' ' + '**' + account_digit[-4:]
    return account

print(date_show("2019-04-12T17:27:27.896421"))