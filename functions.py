# функции запросов
import re
from typing import Iterable, Iterator, Any, List


# filter, получает искомый фрагмент и где искать
def filter_query(value: str, data: Iterable[str]) -> Iterator[str]:
    # возвращает список строк с совпадениями
    return filter(lambda x: value in x, data)


# map, получает номер колонки и где искать
# возвращает обработанные искомые элементы
def map_query(value: str, data: Iterable[str]) -> Iterator[str]:
    # преобразуем номер колонки в число
    column_number: int = int(value)
    # делим строку по пробелам и оставляем кусок строки с номером колонки, который и выводим
    return map(lambda x: x.split(' ')[column_number], data)


# unique, получает строки
def unique_query(data: Iterable[str], *args: Any, **kwargs: Any) -> set[str]:
    # возвращает уникальные строки через множества
    return set(data)


# sort, получает порядок сортировки и что сортировать
def sort_query(value: str, data: Iterable[str]) -> List[str]:
    # по умолчанию сортировка по возрастанию
    reverse: bool = value == 'desc'
    # возвращает отсортированные данные
    return sorted(data, reverse=reverse)


# filter, получает искомый фрагмент и где искать(поиск по регулярным выражениям)
def regex_query(value: str, data: Iterable[str]) -> Iterator[str]:
    pattern: re.Pattern = re.compile(value)
    # возвращает список строк с совпадениями
    return filter(lambda x: re.search(pattern, x), data)
