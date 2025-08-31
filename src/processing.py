def filter_by_state(dict_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""
    filtered_by_state_dict_list = []

    for dict in dict_list:
        for key in dict:
            if dict[key] == state:
                filtered_by_state_dict_list.append(dict)
    return filtered_by_state_dict_list


