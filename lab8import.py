import random
import math

def f1(x1, x2):
    return float(x1) + float(x2)


def f2(x1, x2):
    return x1 - x2


def f3(x1, x2):
    return x1 * x2


def f4(x1, x2):
    return x1 / x2


def f5(x1, x2):
    return pow(x1, x2)


def f6(x):
    return abs(x)


def f7(x1, x2):
    return random.uniform(x1, x2)


def f8(x):
    return math.factorial(x)


def f9(x):
    return math.acos(x)