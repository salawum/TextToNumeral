from NumeralHelper import NumeralHelperClass as helper

x = helper()
input_string = "one hundred eighty-nine trillion four hundred forty-one billion six hundred eighteen million seven hundred sixty-five thousand eight hundred forty-seven"
print(x.word_print(x.tokeniser(input_string)))