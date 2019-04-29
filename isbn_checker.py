import re

class IsbnChecker:
    def __init__(self, isbn):
        self.isbn = self.__sanitize_input(isbn)
        # self.isbn_type = isbn.length == 10 ? 'isbn-10' : 'isbn-13'

    def check(self):
        if len(self.isbn) != 10:
            return False

        sum = 0
        if self.isbn.endswith('X'):
            sum = 100
            self.isbn = self.isbn[:-1]

        for i in range(len(self.isbn)):
            if not self.isbn[i].isdigit():
                return False
            sum += int(self.isbn[i]) * (i + 1)

        return sum % 11 == 0


    def __sanitize_input(self, isbn_input):
        return re.sub('[\s+-]', '', isbn_input)
