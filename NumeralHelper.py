from Numeral import numerals

class NumeralHelperClass:
    def __init__(self):
        self.previousToken = ""
        self.total = 0
        self.pool = 0


    def convert(self, string, formatting=True):
        return self.word_print(self.tokeniser(string), formatting)


    def tokeniser(self, string):
        tokens = string.replace("-"," ").replace(",","").split()
        self.setPreviousToken(tokens[0])
        return tokens


    def word_print(self, tokens, formatting):
        if tokens != []:
            current_token = tokens[0]
            if self.isTokenValid(current_token):
                if self.getValue(self.getPreviousToken()) >= 1000 and current_token != "and":
                    self.increaseTotal(self.getPool())
                    self.setPool(0)
                    self.increasePool(self.getValue(current_token))
                elif self.getValue(current_token) >= 100:
                    self.setPool(self.getPool() * self.getValue(current_token))
                else:
                    self.increasePool(self.getValue(current_token))
            else:
                return f'Token \'{current_token}\' not found'
            self.setPreviousToken(current_token)
            return self.word_print(tokens[1::], formatting)
        self.increaseTotal(self.getPool())
        if not formatting:
            return self.getTotal()
        totalString = str(self.getTotal())
        newString = totalString
        index = 3
        while index < len(totalString):
            newString = newString[:len(totalString)-index] + ',' + newString[len(totalString)-index:]
            index += 3
        return newString


    def getValue(self, token):
        return numerals.get(token)


    def isTokenValid(self, token):
        if token in set(numerals.keys()):
            return True
        return False


    def getTotal(self):
        return self.total


    def increaseTotal(self, value):
        self.total += value


    def getPool(self):
        return self.pool


    def setPool(self, value):
        self.pool = value


    def increasePool(self, value):
        self.pool += value


    def setPreviousToken(self, token):
        self.previousToken = token


    def getPreviousToken(self):
        return self.previousToken