from enum import Enum

numerals = {
    "one": {"value": 1, "denomination": "ONE"},
    "two": {"value": 2, "denomination": "ONE"},
    "three": {"value": 3, "denomination": "ONE"},
    "four": {"value": 4, "denomination": "ONE"},
    "five": {"value": 5, "denomination": "ONE"},
    "six": {"value": 6, "denomination": "ONE"},
    "seven": {"value": 7, "denomination": "ONE"},
    "eight": {"value": 8, "denomination": "ONE"},
    "nine": {"value": 9, "denomination": "ONE"},
    "ten": {"value": 10, "denomination": "TEN"},
    # TODO 
    # 🙃
}

class NumeralType(Enum):
    ONE = 1
    TEN = 10
    HUNDRED = 100
    THOUSAND = 1000
    MILLION = 1000000

class Numerals(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    ELEVEN = 11
    TWELVE = 12
    THIRTEEN = 13
    FOURTEEN = 14
    FIFTEEN = 15
    SIXTEEN = 16
    SEVENTEEN = 17
    EIGHTEEN = 18
    NINETEEN = 19
    TWENTY = 20
    THIRTY = 30
    FORTY = 40
    FIFTY = 50
    SIXTY = 60
    SEVENTY = 70
    EIGHTY = 80
    NINETY = 90
    HUNDRED = 100
    THOUSAND = 1000
    MILLION = 1000000