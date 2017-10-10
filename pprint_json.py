import json
import sys


def load_data(filepath):
    data = ""
    try:
        with open(filepath, "r") as f:
            for line in f:
                data += line
        data = json.loads(data)
        pretty_print_json(data)
    except IOError as e:
        print("Ошибка. Файл не найден.")


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Ошибка. Не указан файл.")
        sys.exit(1)

    if len(sys.argv) > 2:
        print("Ошибка. Слишком много параметров.")
        sys.exit(1)
    filepath = sys.argv[1]
    load_data(filepath)
