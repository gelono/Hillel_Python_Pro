import os
import sqlite3

from typing import List


def execute_query(query_sql: str) -> List:
    '''
    Функция для выполнения запроса
    :param query_sql: запрос
    :return: результат выполнения запроса
    '''
    db_pass = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_pass)
    cur = connection.cursor()
    result = cur.execute(query_sql).fetchall()
    connection.close()
    return result


def unwrapper(records: List) -> None:
    '''
    Функция для вывода результата выполнения запроса
    :param records: список ответа БД
    '''
    for record in records:
        print(*record)


def calculate_profit() -> None:
    """
    Функция выполняет запрос к БД: подсчитывает суммарную прибыль в таблице invoice_items
    """
    query_sql = '''
            SELECT sum(UnitPrice * Quantity)
            FROM invoice_items;
        '''
    return unwrapper(execute_query(query_sql))


def get_non_unique_names() -> None:
    """
    Функция выполняет запрос к БД: возвращает количество неуникальных имен в таблице customers
    """
    query_sql = """
            SELECT FirstName, COUNT(FirstName) amount FROM customers
            GROUP BY FirstName
            HAVING amount > 1;
        """
    return unwrapper(execute_query(query_sql))


if __name__ == '__main__':
    calculate_profit()
    get_non_unique_names()
