

class ClassName:

    def set_up_class_name(self, python_class_name):
        """this returns the class name
        """
        if type(python_class_name) == str:
            try:
                class_name = python_class_name.replace("class", '').replace('{', '')
                self.full_class_dict['class_name_key'] = class_name
                return class_name
            except Exception as e:
                print("PYTHON CLASS NAME ERROR: ")
                print(e)
        else:
            print("ERROR: SETUP CLASS NAME: data type is not corrected ")
            print(type(python_class_name))