import json
import sys


def load_data(filepath):
    try:
        with open(filepath, "r") as file_json:
            str_json = file_json.read()
        if not str_json:
            raise sys.exit("Ошибка: файл пуст.")
        return str_json
    except IOError as err:
        sys.exit("Ошибка: файл не найден.")


def load_json(str_json):
    return json.loads(str_json)


def pretty_print_json(data_json):
    print(json.dumps(data_json, ensure_ascii=False, sort_keys=True, indent=4))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Ошибка: не указан файл.")

    if len(sys.argv) > 2:
        sys.exit("Ошибка: слишком много параметров.")
    filepath = sys.argv[1]
    str_json = load_data(filepath)
    data_json = load_json(str_json)
    pretty_print_json(data_json)
