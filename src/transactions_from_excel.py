import json
import os
from pathlib import Path
from typing import Any, Dict, List, Union

import pandas as pd


def get_transactions_from_excel(file_path: str) -> Union[List[Dict[Any]], str]:
    """функция принимает на вход путь до xlsx-файла и возвращает список транзакций
    + заносит его в ../data/../data/output_excel.json"""

    file_name = os.path.abspath(file_path)

    try:
        excel_data = pd.read_excel(file_name)
        # убираем пустые строки, чтобы они не вызывали ошибок при работе других функций
        excel_data_filtered_from_empty_rows = excel_data.dropna(how='all')
        # преобразуем таблицу в список словарей с доп. вложенностью, по аналогии с предыдущими заданиями
        result_list = excel_data_filtered_from_empty_rows.apply(lambda row: {
            "id": int(row['id']),
            "state": row['state'],
            "date": row['date'],
            "operationAmount": {
                "amount": str(row['amount']),
                "currency": {
                    "name": row['currency_name'],
                    "code": row['currency_code']
                }
            },
            "description": row['description'],
            "from": row['from'] if pd.notna(row['from']) else None,
            "to": row['to'] if pd.notna(row['to']) else None
        }, axis=1).tolist()

    except Exception as e:
        result_list = []
        print(f"Something went wrong: {e}")

    # для удобства просмотра и н всякий случай передаем результат в json
    file_name_json = Path(__file__).parent.parent / 'data' / 'output_excel.json'
    try:
        with open(file_name_json, 'w', encoding='UTF-8') as f:
            json.dump(result_list, f, indent=4)
    except Exception as e:
        return f"Something went wrong with json: {e}"

    return result_list
