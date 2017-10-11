# Prettify JSON

The program prints a JSON file in the console.

# Quickstart

The program in the parameters takes a file name with JSON data.
Example of script launch on Linux, Python 3.5:

```bash
$ python pprint_json.py <path to file>
```

```bash
#The function opens the JSON file and extracts the string
load_data(filepath)
```

```bash
#The function deserializes a string in a Python object
load_json(str_json)
```

```bash
#The function serializes the object into a format string of the JSON format and outputs it to the console in a readable form
pretty_print_json(data_json)
```

The result of the program will be the output of the received data to the console, in an easy-to-read form.
Example of outputting JSON data to the console:

```bash
{
    "board": {
        "cpu": {
            "hz": 12000,
            "model": "80286"
        },
        "image": "http://www.s100computers.com/My%20System%20Pages/80286%20Board/Picture%20of%2080286%20V2%20BoardJPG.jpg",
        "model": "IBM-PC S-100",
        "vendor": "IBM",
        "video": "http://www.s100computers.com/My%20System%20Pages/80286%20Board/80286-Demo3.mp4"
    },
    "floppy": 0,
    "hdd": [
        {
            "size": 33554432,
            "vendor": "Samsung",
            "volume": "C:"
        },
        {
            "size": 16777216,
            "vendor": "Maxtor",
            "volume": "D:"
        },
        {
            "size": 8388608,
            "vendor": "Maxtor",
            "volume": "C:"
        }
    ],
    "height": 21,
    "length": 42,
    "monitor": null,
    "os": "MS-DOS 1.25",
    "ram": {
        "pins": 30,
        "vendor": "CTS",
        "volume": 1048576
    },
    "width": 54
}
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
