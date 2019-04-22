from View.file_writer import FileWriter
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
        self.output_file_name = ''
        self.input_file_name = ''
        self.final_uml_list = []
        self.overall_content = []

    def pass_to_file_handler(self):

        test = FileWriter.file_writer(self.output_file_name, self.final_uml_list)
        return test

    def set_over_string(self, overall_file):
        """This checks to see if there is a class dict
        """
        print(self.overall_content)
        if type(overall_file) == list:
            try:
                for line in overall_file:
                    if ('--' or '..') in line:
                        Relationships.set_up_relationship(type[SetUp], line)
                    elif 'class' in line:
                        ClassName.set_up_class_name(SetUp(), line)
                    elif ':' in line:
                        Attribute.set_up_attribute_name(SetUp(), line)
                    elif '(' in line:
                        Methods.set_up_method_name(SetUp(), line)
                    elif '}' in line:
                        self.full_class_dict['relationship_key'] = self.relationship_list
                        self.full_class_dict['attributes_key'] = self.attribute_list
                        self.full_class_dict['methods_key'] = self.method_list
                        self.overall_content = self.full_class_dict
                        temp_dict = self.full_class_dict.copy()
                        self.final_uml_list.append(temp_dict)
                        self.full_class_dict.clear()
                        self.full_class_dict = {}
                        self.attribute_list = []
                        self.method_list = []
                        self.relationship_list = []
                self.pass_to_file_handler()
            except Exception as e:
                print("OVER STRING ERROR: ")
                print(e)
        else:
            print("ERROR: SETUP OVER STRING: data type is not corrected ")
            print(type(overall_file))
