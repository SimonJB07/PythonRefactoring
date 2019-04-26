

class ClassName:

    @staticmethod
    def set_up_class_name(python_class_name):
        """this returns the class name
        """
        if type(python_class_name) == str:
            try:
                class_name = python_class_name.replace("class", '').replace('{', '')
                return class_name
            except Exception as e:
                print("PYTHON CLASS NAME ERROR: ")
                print(e)
        else:
            print("ERROR: SETUP CLASS NAME: data type is not corrected ")
            print(type(python_class_name))

    @staticmethod
    def class_print(value, output):
        print(f"class {value}:", file=output)