from Model.relationships import Relationships
from Model.class_name import ClassName
from Model.attributes import Attribute
from Model.methods import Methods


class SetUp(object):
    """The class's docstring
    """

    def __init__(self):
        self.full_class_dict = {}
        self.relationship_list = []
        self.attribute_list = []
        self.method_list = []
        self.final_uml_list = []
        self.overall_content = []

    def pass_to_file_handler(self):
        from Controller.main_controller import MainController
        test = self.final_uml_list
        MainController.write_name(test)

    def set_over_string(self, overall_file):
        """This checks to see if there is a class dict
        """
        print("This is be before entering the loop:" )
        print(overall_file)
        if type(overall_file) == list:
            try:
                for line in overall_file:
                    if ('--' or '..') in line:
                        self.relationship_list.append(Relationships.set_up_relationship(line))
                    elif 'class' in line:
                        self.full_class_dict['class_name_key'] = ClassName.set_up_class_name(line)
                    elif ':' in line:
                        self.attribute_list.append(Attribute.set_up_attribute_name(line))
                    elif '(' in line:
                        self.method_list.append(Methods.set_up_method_name(line))
                    elif '}' in line:
                        self.set_keys_value()
                        self.clean_files()
                self.pass_to_file_handler()
            except Exception as e:
                print("OVER STRING ERROR: ")
                print(e)
        else:
            print("ERROR: SETUP OVER STRING: data type is not corrected ")
            print(type(overall_file))

    def set_keys_value(self):
        self.full_class_dict['relationship_key'] = self.relationship_list
        self.full_class_dict['attributes_key'] = self.attribute_list
        self.full_class_dict['methods_key'] = self.method_list

    def clean_files(self):
        self.overall_content = self.full_class_dict
        temp_dict = self.full_class_dict.copy()
        self.final_uml_list.append(temp_dict)
        self.full_class_dict.clear()
        self.full_class_dict = {}
        self.attribute_list = []
        self.method_list = []
        self.relationship_list = []

