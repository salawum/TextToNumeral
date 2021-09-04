from NumeralHelper import NumeralHelperClass as helper
import NumeralHelper
from pprint import pprint

x = helper()
# print(x.getName("sixty"))
# print(x.getType("eighteen"))
# print(x.getValue("eleen"))
# print(x.isTokenValid("test"))
# print(x.isTokenValid("thousand"))
# print(x.getTotal())

input_string = "seven hundred and sixty-three thousand, nine hundred and twenty-four"
x.pront(x.tokeniser(input_string))

# pprint(NumeralHelper.numerals, sort_dicts=False)