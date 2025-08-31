def filter_by_state(user_dict_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""
    filtered_by_state_dict_list = []

    for dict in user_dict_list:
        for key in dict:
            if dict[key] == state:
                filtered_by_state_dict_list.append(dict)
    return filtered_by_state_dict_list


def sort_by_date(user_dict_list: list[dict], sorting_order: bool = True) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание), и возвращает новый список, отсортированный по дате."""
    sorted_user_dict_list = []

    for dict in user_dict_list:
        sorted_user_dict_list = sorted(user_dict_list, key=lambda dict: dict["date"], reverse=sorting_order)
    return sorted_user_dict_list
