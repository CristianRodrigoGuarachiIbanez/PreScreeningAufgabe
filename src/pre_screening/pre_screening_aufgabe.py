
from time import sleep
from datetime import datetime, time, date
from sys import exit
import pytz
from babel.dates import format_date
tz_germany = pytz.timezone('Europe/Berlin')


class DDATES:
    def __init__(self, dates, times):
        self.dates = dates
        self.times = times


def get_input_number(eingabe):
    versuche = 0
    while not (eingabe.isnumeric()):
        if (versuche == 3):
            exit()
        versuche += 1
        print("[Error] das Argument muss eine Zahl zwischen 1 und 10 sein!")
        print(" Versuchen Sie es nochmal")
        eingabe = input("Wie viel Daten möchten Sie eingeben? ")

    return int(eingabe.strip())

def get_date(num, inputt=None):
    i = 0
    DATES = []
    tt, mm, jjjj = (0, 0, 0)
    while (i < num):
        if (inputt is None):
            try:
                datum = input("Bitte Geben Sie ein Datum ein: ")
            except Exception:
                exit()
        else:
            datum = inputt[i]
            datum = datum.split(" ")[0]
        try:
            _datum = datum.strip().split(".")
            tt, mm, jjjj = int(_datum[0]), int(_datum[1]), int(_datum[-1])
        except Exception:
            print("Nur das Format TT.DD.JJJJ ist erlaubt")
            exit()

        _datum_ = date(jjjj, mm, tt)
        if (inputt is None):
            zeit = input("Bitte geben Sie eine Zeit ein: ")
        else:
            zeit = inputt[i]
            zeit = zeit.split(" ")[1]
        _zeit = zeit.strip().split(":")
        h, m = int(_zeit[0]), int(_zeit[1])
        _zeit_ = time(h, m)
        dates = DDATES(_datum_, _zeit_)
        DATES.append(dates)
        i += 1
    return DATES


def get_days(num, inputt=None):
    dates = get_date(num, inputt)
    now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    inSek = []
    for i in range(len(dates)):
        datum = dates[i].dates
        hh = dates[i].times
        jetzt = datetime.strptime(now, '%Y-%m-%d %H:%M:%S')
        stunden = datetime.combine(datum, hh) - jetzt
        inSek.append(stunden.seconds)
        print("EINGABE ->", hh, " JETZIGE ZEIT -> ", jetzt, " DIFFERENZ IN SEK -> ", stunden.seconds)
    return inSek, dates


def make_sleep(seks, dates):
    for i in range(len(seks)):
        sleep(seks[i])
        datum = format_date(dates[i].dates, "dd.MM.yyyy", locale='de')
        print("Das {}  Datum wurde erreicht! ({} - {})".format(i+1, datum, dates[i].times))


if (__name__ == "__main__"):
    pass
