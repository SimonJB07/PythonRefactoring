from Model.replace_value import Replace

import re


class FormatData:

    @staticmethod
    def format_relationship(data):
        for word in data.strip().split():
            if ':' not in word:
                word = re.findall('[A-Z][^A-Z]*', word)
                add_line = word[0] + "_" + word[1]
                lower_case = add_line.lower()
                string_all = lower_case + ': ' + add_line.replace("_", '')
                return string_all

    @staticmethod
    def reverse_words(word):
        """this reverse words in a string
        """
        if type(word) == str:
            return ' '.join(reversed(word.split()))
        else:
            print("ERROR: SETUP REVERSE WORD: data type is not corrected ")
            print(type(word))

    @staticmethod
    def clear_up_data(data):
        """this converts to a class diagram str
        """
        if type(data) == str:
            try:
                clean_data = data.replace('String', Replace.STRING.value) \
                    .replace('int', Replace.INTEGER.value) \
                    .replace('Float', Replace.FLOAT.value) \
                    .replace('Boolean', Replace.BOOLEAN.value) \
                    .replace('List', Replace.LIST.value) \
                    .replace('Tuple', Replace.TUPLE.value) \
                    .replace('Dict', Replace.DICT.value)
            except Exception as e:
                print("VALUE ERROR: ")
                print(e)
            finally:
                return clean_data
        else:
            print("ERROR: SETUP CLEAR UP DATA: data type is not corrected ")
            print(type(data))

