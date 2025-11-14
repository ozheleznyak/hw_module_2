import json
import os
from pathlib import Path
from typing import Any

import pandas as pd


def get_transactions_from_csv(file_path: str) -> Any:
    """функция принимает на вход путь до csv-файла и возвращает список транзакций
    + заносит его в ../data/../data/output_csv.json"""

    file_name = os.path.abspath(file_path)
    result_list = []

    try:
        csv_data = pd.read_csv(file_name, sep=';', skip_blank_lines=True, dtype={'id': 'Int64'})

        for index, row in csv_data.iterrows():
            record = {
                "id": int(row['id']) if pd.notna(row['id']) else None,
                "state": str(row['state']) if pd.notna(row['state']) else "",
                "date": str(row['date']) if pd.notna(row['date']) else "",
                "operationAmount": {
                    "amount": str(row['amount']) if pd.notna(row['amount']) else "",
                    "currency": {
                        "name": str(row['currency_name']) if pd.notna(row['currency_name']) else "",
                        "code": str(row['currency_code']) if pd.notna(row['currency_code']) else ""
                    }
                },
                "description": str(row['description']) if pd.notna(row['description']) else "",
                "from": str(row['from']) if pd.notna(row['from']) and row['from'] != '' else "",
                "to": str(row['to']) if pd.notna(row['to']) else ""
            }
            result_list.append(record)

    except Exception as e:
        result_list = []
        print(f"Something went wrong: {e}")

    file_name_json = Path(__file__).parent.parent / 'data' / 'output_csv.json'
    try:
        with open(file_name_json, 'w', encoding='UTF-8') as f:
            json.dump(result_list, f, indent=4)
    except Exception as e:
        return f"Something went wrong with json: {e}"

    return result_list
