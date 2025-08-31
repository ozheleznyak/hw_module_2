def filter_by_state(dict_list: list, state='EXECUTED') -> list:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""
    filtered_by_state_dict_list = []

    for dict in dict_list:
        for key in dict:
            if dict[key] == state:
                filtered_by_state_dict_list.append(dict)
    return filtered_by_state_dict_list


dict_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

print(filter_by_state(dict_list, "CANCELED"))
git