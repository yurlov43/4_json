# Prettify JSON

The program prints a JSON file in the console.

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash
$ python pprint_json.py <path to file>
```

The program in the parameters takes a file name with JSON data:

```bash
load_data(filepath) #The function deserializes JSON from a file
```

The result of the program will be the output of the received data to the console, in an easy-to-read form:

```bash
pretty_print_json(data) #The function serializes obj into a JSON-format string
```

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
