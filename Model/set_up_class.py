from View.file_writer import FileWriter
from Model.replace_value import Replace
from Model.relationship_value import Relationship
from Model.format_data import FormatData


class SetUp:
    """The class's docstring
    """
    uml_list = []
    class_dict = {}
    class_relationship = []
    attribute_list = []
    method_list = []
    file_setup_name = ''
    overall_content = []

    @staticmethod
    def pass_file():

        test = FileWriter.file_writer(SetUp.file_setup_name, SetUp.uml_list)
        return test

    @staticmethod
    def set_over_string(overall_file):
        """This checks to see if there is a class dict
        """

        if type(overall_file) == list:
            try:
                for line in overall_file:
                    if ('--' or '..') in line:
                        SetUp.set_up_relationship(line)
                    elif 'class' in line:
                        SetUp.set_up_class_name(line)
                    elif ':' in line:
                        SetUp.set_up_attribute_name(line)
                    elif '(' in line:
                        SetUp.set_up_method_name(line)
                    elif '}' in line:
                        SetUp.class_dict['relationship_key'] = SetUp.class_relationship
                        SetUp.class_dict['attributes_key'] = SetUp.attribute_list
                        SetUp.class_dict['methods_key'] = SetUp.method_list
                        SetUp.overall_content = SetUp.class_dict
                        temp_dict = SetUp.class_dict.copy()
                        SetUp.uml_list.append(temp_dict)
                        SetUp.class_dict.clear()
                        SetUp.class_dict = {}
                        SetUp.attribute_list = []
                        SetUp.method_list = []
                        SetUp.class_relationship = []
                SetUp.pass_file()
            except Exception as e:
                print("OVER STRING ERROR: ")
                print(e)
        else:
            print("ERROR: SETUP OVER STRING: data type is not corrected ")
            print(type(overall_file))

    @staticmethod
    def set_up_class_name(python_class_name):
        """this returns the class name
        """
        if type(python_class_name) == str:
            try:
                class_name = python_class_name.replace("class", '').replace('{', '')
                SetUp.class_dict['class_name_key'] = class_name
                return class_name
            except Exception as e:
                print("PYTHON CLASS NAME ERROR: ")
                print(e)
        else:
            print("ERROR: SETUP CLASS NAME: data type is not corrected ")
            print(type(python_class_name))

    @staticmethod
    def set_up_attribute_name(attribute_name):
        """This changes String into the str or the diagram
        """
        if type(attribute_name) == str:
            try:
                temp_att = SetUp.clear_up_data(attribute_name)
                at = SetUp.reverse_words(temp_att)
                SetUp.attribute_list.append(at)
                return temp_att
            except Exception as e:
                print("ATTRIBUTE NAME ERROR: ")
                print(e)
        else:
            print("ERROR: SETUP ATTRIBUTE NAME: data type is not corrected ")
            print(type(attribute_name))

    @staticmethod
    def set_up_method_name(method_name):
        """this removes the String from the method attributes
        """
        if type(method_name) == str:
            try:
                temp_met = method_name.replace('void', '')
                met = SetUp.clear_up_data(temp_met).replace('str ', '')
                SetUp.method_list.append(met)
                return met
            except Exception as e:
                print("METHOD NAME ERROR: ")
                print(e)
        else:
            print("ERROR: SETUP METHOD NAME: data type is not corrected ")
            print(type(method_name))


    @staticmethod
    def set_up_relationship(relationship_value):
        """this method converts diagram to workable class
        """

        if type(relationship_value) == str:
            try:
                temp_rel = SetUp.clean_up_relationship(relationship_value)
                clean_string = FormatData.format_relationship(temp_rel)
                SetUp.class_relationship.append(clean_string)
                return clean_string
            except Exception as e:
                print("RELATIONSHIP VALUE ERROR: ")
                print(e)
        else:
            print("ERROR: SETUP RELATIONSHIP: data type is not corrected ")
            print(type(relationship_value))


    @staticmethod
    def clean_up_relationship(relationship):
        """this picks out the right value for the relationship
        """
        if type(relationship) == str:
            try:
                relation = relationship.replace("<|--", Relationship.EXTENSION.value) \
                    .replace('*--', Relationship.COMPOSITION.value) \
                    .replace('o--', Relationship.AGGREGATION.value) \
                    .replace('-->', Relationship.DIRECTED_ASSOCIATION.value) \
                    .replace("..|>", Relationship.IMPLEMENTATION.value) \
                    .replace('<--*', Relationship.COMPOSITION_ASSOCIATION.value) \
                    .replace('..>', Relationship.DEPENDENCY.value) \
                    .replace('x--', Relationship.CONTAINMENT.value) \
                    .replace('}--', Relationship.CROWS_FEET.value) \
                    .replace('^--', Relationship.INTERFACE.value) \
                    .replace("..", Relationship.INHERITANCE.value) \
                    .replace("--", Relationship.ASSOCIATION.value)
            except Exception as e:
                print("RELATIONSHIP ERROR: ")
                print(e)
            finally:
                return relation
        else:
            print("ERROR: CLEAN RELATIONSHIP: data type is not corrected ")
            print(type(relationship))

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

