from functions import filter_query, map_query, unique_query, sort_query
from typing import Optional, Iterable
# связываем команды с функциями
CMD_TO_FUNCTION = {
    'filter': filter_query,
    'unique': unique_query,
    'map': map_query,
    'sort': sort_query
}


# функция чтения файла по строчно
def read_file(file_name: str):
    with open(file_name) as f:
        for line in f:
            yield line


# конструктор запроса, формирует запрос на основе полученных данных
def constructor_query(cmd, value, file_name, data: Optional[Iterable[str]]):
    if data is None:
        prepared_data = read_file(file_name)
    else:
        prepared_data = data

    func_result = CMD_TO_FUNCTION[cmd](param=value, data=prepared_data)

    return list(func_result)


