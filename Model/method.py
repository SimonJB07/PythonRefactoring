from Controller.main_error_checker import ErrorChecker
from Model.format_data import FormatData


class Method:

    @staticmethod
    def error_check_method(method_name):
        """this removes the String from the method attributes
        """
        ErrorChecker.error_type(str, method_name, "SETUP METHOD NAME: data type is not corrected")
        try:
            return Method.method_clean(method_name)
        except Exception as e:
            print("METHOD NAME ERROR: ")
            print(e)

    @staticmethod
    def method_clean(method_data):
        temp_met = method_data.replace('void', '')
        return FormatData.clear_up_data(temp_met).replace('str ', '')

    @staticmethod
    def methods_print(value, output):
        stat = "staticmethod"
        for methods in value:
            rep_met = methods
            if "(name)" in rep_met:
                rep_met = methods.replace('(name)', '(self, name)')
            if "self" not in rep_met:
                print(f"    @{stat}", file=output)
            print(f"    def {rep_met}:", file=output)
            print(f"        pass\n", file=output)
