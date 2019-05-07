'''
1. Создайте классы Noun и Verb.
2. Настройте наследование от Word.
3. Добавьте защищенное свойство «Грамматические характеристики».
4. Перестройте работу метода show класса Sentence.
5. Перестройте работу метода show_part класса Sentence, чтобы он показывал грамматические характеристики.
'''





class Word:

    def __init__(self, text='', part_of_speech=''):
        self.text = text
        self.part_of_speech = part_of_speech


class Noun(Word):

    def __init__(self, text='', part_of_speech='Существительное'):
        self.text = text
        self.__gram_params = 'род, число, падеж, склонение'
        super().__init__(text, part_of_speech)

    def get_gram_params(self):
        return self.__gram_params


class Verb(Word):

    def __init__(self, text='', part_of_speech='Глагол',):
        self.text = text
        self.__gram_params = 'число, время, наклонение'
        super().__init__(text, part_of_speech)

    def get_gram_params(self):
        return self.__gram_params


class Sentence:
    def __init__(self, words=[], content=[]):
        self.words = words
        self.content = content

    def show(self):
        ls = [self.words[i].text for i in self.content]
        s=' '.join(ls)
        return s.capitalize()


    def show_parts(self):
        result = {}
        for i in self.content:
            result[self.words[i].text] = self.words[i].get_gram_params()

        return result


s = Sentence([Noun('куст'), Noun('сирени'), Verb('цветет')], [0, 1, 2])

print(s.show())

print(s.show_parts())
