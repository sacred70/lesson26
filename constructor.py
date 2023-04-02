from functions import filter_query, map_query, unique_query, sort_query, regex_query
from typing import Optional, Iterable, List, Callable
# связываем команды с функциями
CMD_TO_FUNCTION: dict[str, Callable] = {
    'filter': filter_query,
    'unique': unique_query,
    'map': map_query,
    'sort': sort_query,
    'regex': regex_query
}


# функция чтения файла по строчно
def read_file(file_name: str) -> Iterable[str]:
    with open(file_name) as f:
        for line in f:
            yield line


# конструктор запроса, формирует запрос на основе полученных данных
def constructor_query(cmd: str, value: str, file_name: str, data: Optional[Iterable[str]]) -> List[str]:
    if data is None:
        prepared_data: Iterable[str] = read_file(file_name)
    else:
        prepared_data = data

    func: Callable = CMD_TO_FUNCTION[cmd]
    func_result: Iterable[str] = func(param=value, data=prepared_data)

    return list(func_result)


