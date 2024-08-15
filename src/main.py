from config import operations_path
import src.utils


def main():
    def get_five_transactions():
        '''Возвращает 5 последних транзакций с заданными условиями'''
        showed_transactions = []
        for el in range(5):
            showed_transactions.append(src.utils.get_sorted_transactions()[el])

        return showed_transactions

    def output_transactions():
        '''Выводит результат в необходимом формате'''
        output_str = ''
        for el in get_five_transactions():
            output_str_1 = (f'{src.utils.show_date(el.get("date"))} '
                            f'{el.get("description")}\n')

            if src.utils.get_card_number(el.get('from')) is None:
                if el.get('to')[0:2] == 'Сч':
                    output_str_2 = f'{src.utils.get_account_number(el.get("to"))}\n'
                else:
                    output_str_2 = f'{src.utils.get_card_number(el.get("to"))}\n'
            else:
                if el.get('from')[0:2] == 'Сч' and el.get('to')[0:2] == 'Сч':
                    output_str_2 = (
                        f'{src.utils.get_account_number(el.get("from"))} --> '
                        f'{src.utils.get_account_number(el.get("to"))}\n')
                elif el.get('from')[0:2] != 'Сч' and el.get('to')[0:2] == 'Сч':
                    output_str_2 = (
                        f'{src.utils.get_card_number(el.get("from"))} --> '
                        f'{src.utils.get_account_number(el.get("to"))}\n')
                else:
                    output_str_2 = (
                        f'{src.utils.get_card_number(el.get("from"))} --> '
                        f'{src.utils.get_card_number(el.get("to"))}\n')

            output_str_3 = (f'{el.get("operationAmount").get("amount")} '
                            f'{el.get("operationAmount").get("currency").get("name")}\n')

            output_str += output_str_1 + output_str_2 + output_str_3 + '\n'

        return output_str

    print(output_transactions())


if __name__ == '__main__':
    main()
