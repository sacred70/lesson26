# функции запросов

# filter, получает искомый фрагмент и где искать
def filter_query(desired, list_text):
    # возвращает список строк с совпадениями
    return list(filter(lambda x: desired in x, list_text))


# map, получает номер колонки и где искать
# возвращает обработанные искомые элементы
def map_query(value, data):
    # преобразуем номер колонки в число
    column_number = int(value)
    # делим строку по пробелам и оставляем кусок строки с номером колонки, который и выводим
    return map(lambda x: x.split(' ')[column_number], data)