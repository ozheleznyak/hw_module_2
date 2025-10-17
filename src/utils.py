import json

def get_transaction_list(file_path: str) -> list:
    transaction_list = []

    try:
        with open(file_path, encoding="UTF-8") as json_file:
            transaction_list = json.load(json_file)
        return transaction_list
    except json.JSONDecodeError:
        return transaction_list
    except TypeError:
        return transaction_list
    except ValueError:
        return transaction_list
    except FileNotFoundError:
        return transaction_list
