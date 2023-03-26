# функции запросов

# фильтр, получает исковый фрагмент и где искать
# возвращает список строк с совпадениями
def filter_query(desired, list_text):
    return list(filter(lambda x: desired in x, list_text))


