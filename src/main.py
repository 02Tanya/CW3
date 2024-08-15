from config import operations_path
import src.utils


def main():
    def get_five_transactions(operation_path):
        '''Возвращает 5 последних транзакций с заданными условиями'''
        showed_transactions = []
        for el in range(5):
            showed_transactions.append(src.utils.get_sort_transaction(operation_path)[el])
        return showed_transactions

    def get_transaction(operation_path):
        '''Выводит результат в необходимом формате'''
        output_str = ''
        for el in get_five_transactions(operation_path):
            output_str_1 = (f'{src.utils.date_show(el.get("date"))} '
                            f'{el.get("description")}\n')

            if src.utils.format_from_account(el.get('from')) is None:
                if el.get('to')[0:2] == 'Сч':
                    output_str_2 = f'{src.utils.format_to_account(el.get("to"))}\n'
                else:
                    output_str_2 = f'{src.utils.format_from_account(el.get("to"))}\n'
            else:
                if el.get('from')[0:2] == 'Сч' and el.get('to')[0:2] == 'Сч':
                    output_str_2 = (
                        f'{src.utils.format_to_account(el.get("from"))} --> '
                        f'{src.utils.format_to_account(el.get("to"))}\n')
                elif el.get('from')[0:2] != 'Сч' and el.get('to')[0:2] == 'Сч':
                    output_str_2 = (
                        f'{src.utils.format_from_account(el.get("from"))} --> '
                        f'{src.utils.format_to_account(el.get("to"))}\n')
                else:
                    output_str_2 = (
                        f'{src.utils.format_from_account(el.get("from"))} --> '
                        f'{src.utils.format_from_account(el.get("to"))}\n')

            output_str_3 = (f'{el.get("operationAmount").get("amount")} '
                            f'{el.get("operationAmount").get("currency").get("name")}\n')

            output_str += output_str_1 + output_str_2 + output_str_3 + '\n'

        return output_str

    print(get_transaction(operations_path))


if __name__ == '__main__':
    main()
