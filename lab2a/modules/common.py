import datetime
import sys
from logging import *

logger = getLogger()


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform

def Pair(bol):
    for i in range(0,100):
        if(bol and i%2 == 0):
            print(i)
        elif(not bol and i%2 != 0):
            print(i)
def TwoDivideOn(num):
    try:
        a = 2/num
        logger.error("Програма виконалась")
        return a
    except Exception as ERROR:
        logger.error("Помилка")
