
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
