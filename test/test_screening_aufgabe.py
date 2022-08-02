from pre_screening.pre_screening_aufgabe import *
import argparse
import pytest


def current_time(heute, index):
    heute = heute.split(" ")
    today = heute[0].split(".")
    today = today[2] +"."+ today[1]+"."+today[0]
    zeit = heute[1].split(":")
    hh,mm,ss = int(zeit[0]),int(zeit[1]),0
    output = []
    for i in range(index):
        if(mm>=59):
            mm=00
            if(hh==24 or hh==00):
                hh=1
            else:
                hh += 1
        else:
            mm +=2
            if(mm>=59):
                mm = 00
        hour = today + " " + str(hh)+":"+str(mm)+":"+zeit[2] +"\n"
        output.append(hour)
    return output


def create_examples():
    filename="example"
    for i in range(0,25, 5):
        if(i==0):
            i+=1
        name = filename + str(i) +".txt"
        today = datetime.today().strftime('%Y.%m.%d %H:%M:%S')
        examples = current_time(today, i)
        with open(name, "w") as file:
            for line in examples:
                file.write(line)
            file.close()

def _make_sleep(num=None):
    create_examples()
    filename = None
    flag1, flag2, flag3, flag4,flag5 = None, None, None, None, None
    parser=argparse.ArgumentParser()
    # parser.add_argument("-dates", "--num_dates", type=int)
    # args = parser.parse_args()
    # num = args.num_dates
    if(num is None):
        num = input("Wie viele Daten möchten Sie eingeben? ")
        num = get_input_number(num)
    if(num==1):
        parser.add_argument("--input1", action="store", default="example1.txt")
        flag1 = True
    elif(num==5):
        parser.add_argument("--input2", action="store", default="example5.txt")
        flag2 = True
    elif(num==10):
        parser.add_argument("--input3", action="store", default="example10.txt")
        flag3 = True
    elif (num == 15):
        parser.add_argument("--input4", action="store", default="example15.txt")
        flag4 = True
    elif(num==20):
        parser.add_argument("--input5", action="store", default="example20.txt")
        flag5 = True
    else:
        print("Bitte geben Sie eine der folgengen Zahlen 1, 5, 10, 15, 20 ein")
        exit()
    args = parser.parse_args()
    if(flag1):
        filename = args.input1
    elif(flag2):
        filename = args.input2
    elif(flag3):
        filename = args.input3
    elif (flag4):
        filename = args.input4
    elif (flag5):
        filename = args.input5

    with open(filename) as file:
        line = file.readlines()
        seks, dates = get_days(num, line)
        make_sleep(seks, dates)

@pytest.mark.parametrize("num", [1,5,10])
def test_make_sleep(num):
    _make_sleep(num)


if(__name__ == "__main__"):
    _make_sleep()