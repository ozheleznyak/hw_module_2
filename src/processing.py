def filter_by_state(user_dict_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""

    filtered_by_state_dict_list = []

    for item in user_dict_list:
        if item["state"] == state.upper():
            filtered_by_state_dict_list.append(item)
    return filtered_by_state_dict_list


def sort_by_date(user_dict_list: list[dict], sorting_order: bool = True) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание), и возвращает новый список, отсортированный по дате."""

    return sorted(user_dict_list, key=lambda dictionary: dictionary["date"], reverse=sorting_order)
