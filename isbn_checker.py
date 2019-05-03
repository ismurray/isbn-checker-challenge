import re

class IsbnChecker:
    def __init__(self, isbn):
        self.isbn = self.__sanitize_input(isbn)

    def check(self):
        if len(self.isbn) == 10:
            return self.__check_10()
        elif len(self.isbn) == 13:
            return self.__check_13()
        else:
            return False

    def __sanitize_input(self, isbn_input):
        return re.sub('[\s+-]', '', isbn_input)

    def __check_10(self):
        sum = 0
        if self.isbn.endswith('X'):
            sum = 100
            self.isbn = self.isbn[:-1]

        for i in range(len(self.isbn)):
            if not self.isbn[i].isdigit():
                return False
            sum += int(self.isbn[i]) * (i + 1)

        return sum % 11 == 0

    def __check_13(self):
        sum = 0

        for i in range(len(self.isbn)):
            if not self.isbn[i].isdigit():
                return False

            if (i + 1) % 2 == 1:
                sum += int(self.isbn[i])
            elif (i + 1) % 2 == 0:
                sum += int(self.isbn[i]) * 3

        return (10 - (sum % 10)) % 10 == 0
