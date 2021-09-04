from Numeral import numerals

class NumeralHelperClass:
    def __init__(self):
        self.previousToken = ""
        self.total = 0
        self.pool = 0


    def tokeniser(self, string):
        return string.replace("-"," ").replace(",","").split()


    def pront(self, tokens):
        if tokens != []:
            token = tokens[0]
            print(token)
            if self.isTokenValid(token):
                # TODO
                # Proper Rules go here
                # Get rid of the token reversal
                # In the example given, we could just assume that if the previousToken was a hundred
                # or a thousand and the current token isn't 'and', we can add the current pool to the
                # total and start a new pool
                self.increaseTotal(self.getValue(token))
                self.getTotal()
            self.updateToken(token)
            self.pront(tokens[1::])


    def getName(self, token):
        return token


    def getValue(self, token):
        try:
            return numerals.get(token).get("value")
        except AttributeError:
            return f'No value found for token: \'{token}\''


    def getType(self, token):
        try:
            return numerals.get(token).get("denomination")
        except AttributeError:
            return f'No type found for token: \'{token}\''


    def isTokenValid(self, token):
        if token in set(numerals.keys()):
            return True
        return False


    def getTotal(self):
        print(self.total)
        return self.total


    def increaseTotal(self, value):
        self.total += value
        return self.total

    # Not tested
    def updateToken(self, token):
        self.previousToken = token