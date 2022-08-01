
from time import sleep
from datetime import datetime, time, date
from babel.dates import format_date
from sys import exit
import pytz
tz_germany = pytz.timezone('Europe/Berlin')
def get_input_number():
    eingabe = input("Wie viel Daten möchten Sie eingeben? ")
    versuche=0
    while not (eingabe.isnumeric()):
        if(versuche==3):
            exit()
        versuche += 1
        print("[Error] das Argument muss eine Zahl zwischen 1 und 10 sein!")
        print(" Versuchen Sie es nochmal")
        eingabe = input("Wie viel Daten möchten Sie eingeben? ")

    return int(eingabe.strip())

def get_date():
    num = get_input_number()
    i=0
    DATES = []
    while(i<num):
        dates=[]
        datum = input("Bitte Geben Sie ein Datum ein: ")
        datum = datum.strip().split(".")
        tt, mm, jjjj = int(datum[0]), int(datum[1]), int(datum[-1])
        datum = date(jjjj, mm, tt)
        #datum = format_date(datum, "dd.MM.yyyy", locale='ger')

        dates.append(datum)
        zeit = input("Bitte geben Sie eine Zeit ein: ")
        zeit = zeit.strip().split(":")
        h,m = int(zeit[0]), int(zeit[1])
        zeit = time(h, m)
        dates.append(zeit)
        DATES.append(dates)
        i+=1
    return DATES
def get_days():
    dates = get_date()
    #heute = date.today()
    now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    inSek= []
    for i in range(len(dates)):
        datum = dates[i][0]
        #tage = heute - datum
        hh = dates[i][1]
        jetzt =  datetime.strptime(now, '%Y-%m-%d %H:%M:%S')#"%H:%M:%S")
        stunden =  datetime.combine(datum, hh)- jetzt
        inSek.append(stunden.seconds)
        print("h ->", hh, "now -> ", jetzt,"stunden -> ",stunden.seconds)
    return inSek, dates
def make_sleep(seks, dates):
    for i in range(len(seks)):
        sleep(seks[i])
        print("Das {}  Datum wurde erreicht! ({} - {})".format(i+1, dates[i][0], dates[i][1]))


if(__name__=="__main__"):
    seks, dates = get_days()
    make_sleep(seks, dates)