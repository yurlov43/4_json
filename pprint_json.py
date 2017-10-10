import json
import sys


def load_data(filepath):
    try:
        with open(filepath, "r") as file_json:
            data_json = json.load(file_json)
        pretty_print_json(data_json)
    except IOError as error:
        print("Ошибка. Файл не найден.")


def pretty_print_json(data_json):
    print(json.dumps(data_json, sort_keys=True, indent=4))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Ошибка. Не указан файл.")
        sys.exit(1)

    if len(sys.argv) > 2:
        print("Ошибка. Слишком много параметров.")
        sys.exit(1)
    filepath = sys.argv[1]
    load_data(filepath)
