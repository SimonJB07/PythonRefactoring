from Controller.main_error_checker import ErrorChecker
from Model.format_data import FormatData


class Attribute:

    @staticmethod
    def set_up_attribute_name(attribute_name):
        """This changes String into the str or the diagram
        """
        ErrorChecker.error_type(str, attribute_name, "ATTRIBUTE NAME: datatype not corrected ")
        try:
            temp_att = FormatData.clear_up_data(attribute_name)
            format_attribute = FormatData.reverse_words(temp_att)
            return format_attribute
        except Exception as e:
            print("ATTRIBUTE NAME ERROR: ")
            print(e)

    @staticmethod
    def attribute_print(value, output):
        for attributes in value:
            print(f"        self.{attributes}", file=output)
        print(f"        ", file=output)
