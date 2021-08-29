# from Numeral import NumeralType
# from Numeral import Numerals
from Numeral import numerals



def pront(token, val):
    pass
    # for num in NumeralType:
    #     if token.lower() == num.name.lower():
    #         print(num.value)
    # for num in Numerals:
    #     print(f'{num.name.lower()}: {num.value}')

    # TODO
    # Pass all the each token in and return the outputted value, being
    # sure to pass the returned result as the input (recursive)


def getName(token):
    return token


def getValue(token):
    return numerals.get(token).get("value")


def getType(token):
    return numerals.get(token).get("denomination")


def isTokenValid(token):
    if token in set(numerals.keys()):
        return True
    return False