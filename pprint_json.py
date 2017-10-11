import json
import sys
import os.path


def load_data(filepath):
    with open(filepath, "r") as file_json:
        return file_json.read()


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
    if not os.path.exists(filepath):
        sys.exit("Ошибка: файл не найден.")
    str_json = load_data(filepath)
    if not str_json:
        sys.exit("Ошибка: файл пустой.")
    data_json = load_json(str_json)
    pretty_print_json(data_json)
