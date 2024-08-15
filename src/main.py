from config import operations_path
import src.utils


def main():
    def five_transactions(json_path):
        '''Возвращает 5 последних транзакций с заданными условиями'''
        showed_transactions = []
        for el in range(5):
            showed_transactions.append(src.utils.get_sort_transaction(json_path)[el])
        return showed_transactions

    def get_transaction(json_path):
        info_str = ''
        for el in five_transactions(json_path):
            info_str_1 = (f'{src.utils.date_show(el.get("date"))}'
                          f'{el.get("description")}\n')

            if src.utils.format_from_account(el.get('from')) is None:
                info_str_2 = f'{src.utils.format_to_account(el.get("to"))}\n'
            else:
                info_str_2 = (
                    f'{src.utils.format_from_account(el.get("from"))} '
                    f'{src.utils.format_to_account(el.get("to"))}\n')
            info_str_3 = (f'{el.get("operationAmount").get("amount")} '
                          f'{el.get("operationsAmount").get("currency").get("name")}\n')

            info_str += info_str_1
            info_str += info_str_2
            info_str += info_str_3 + '\n'

        return info_str

    print(get_transaction(operations_path))


if __name__ == '__main__':
    main()
