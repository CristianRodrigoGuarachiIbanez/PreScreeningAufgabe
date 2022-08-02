from pre_screening.pre_screening_aufgabe import *
import argparse
import pytest
from datetime import datetime
import os


def current_time(heute, index):
    heute = heute.split(" ")
    today = heute[0].split(".")
    today = today[2] + "." + today[1] + "." + today[0]
    zeit = heute[1].split(":")
    hh, mm = int(zeit[0]), int(zeit[1])
    output = []
    for i in range(index):
        if (mm >= 59):
            mm = 00
            if (hh == 24 or hh == 00):
                hh = 1
            else:
                hh += 1
        else:
            mm += 2
            if (mm >= 59):
                mm = 00
        hour = today + " " + str(hh) + ":" + str(mm)+":" + zeit[2] + "\n"
        output.append(hour)
    return output


def create_examples(index=1):
    path = os.path.dirname(os.path.realpath(__file__))
    print(path)
    filename = path + "/example"
    name = filename + str(index) + ".txt"
    today = datetime.today().strftime('%Y.%m.%d %H:%M:%S')
    examples = current_time(today, index)
    with open(name, "w") as file:
        for line in examples:
            file.write(line)
        file.close()


def _make_sleep(num=None, filename=None):

    if (num is None):
        num = input("Wie viele Daten möchten Sie eingeben? ")
        num = get_input_number(num)

    create_examples(num)

    if (filename is None):
        path = os.path.dirname(os.path.realpath(__file__))
        if (num == 1):
            filename = path + "/example1.txt"
        elif (num == 5):
            filename = path + "/example5.txt"
        elif (num == 10):
            filename = path + "/example10.txt"
        elif (num == 15):
            filename = path + "/example15.txt"
        elif (num == 20):
            filename = path + "/example20.txt"
        else:
            print("Bitte geben Sie eine der folgengen Zahlen 1, 5, 10, 15, 20 ein")
            exit()

    with open(filename) as file:
        line = file.readlines()
        seks, dates = get_days(num, line)
        make_sleep(seks, dates)


@pytest.mark.parametrize("num", [1, 5])
def test_make_sleep(num):
    _make_sleep(num)


if (__name__ == "__main__"):
    parser = argparse.ArgumentParser()
    parser.add_argument("-dates", "--num_dates", type=int)
    args = parser.parse_args()
    if not (args.num_dates is None):
        num = args.num_dates[:]
    else:
        num = None
    parser.add_argument("--input", action="store")
    args = parser.parse_args()
    if not (args.input is None):
        filename = args.input[:]
    else:
        filename = None

    _make_sleep(num, filename)
